import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.read_config_utils import Config
from common.log_utils import logger

current_path = os.path.dirname(__file__)
screentshop_path = os.path.join(current_path,'..')
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开网页，网页链接是：%s' % url)

    def quit_browser(self):
        self.driver.quit()
        logger.info('关闭浏览器')

    def input(self,element_info,content):
        element = self.find_element(element_info)
        try:
            element.send_keys(content)
            logger.info('%s元素输入内容，输入的内容是：%s' % (element_info['element_name'],content))
        except Exception as e:
            logger.error('[%s]元素输入内容失败,原因是：%s' % (element_info['element_name'],e))

    def find_element(self,element_info):
        try:
            element_name = element_info['element_name']
            element_type_name = element_info['element_type']
            element_value = element_info['element_value']
            timeout = element_info['timeout']
            if element_type_name == 'xpath':
                element_type = By.XPATH
            element = WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(element_type,element_value))
            logger.info('元素识别成功，元素名称是：%s' % element_name)
        except Exception as e:
            logger.error('[%s]元素识别失败' % element_name)
        return element

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('%s元素点击成功'% element_info['element_name'])

    def timeout(self,timeout=Config.get_timeout):
        '''固定等待'''
        time.sleep(timeout)

    def wait(self,timeout=Config.get_timeout):
        '''隐式等待'''
        self.driver.implicitly_wait(timeout)

    def screentshot(self,screent_shot_path=Config.get_screentshot_path):
        '''截图'''
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screentshot_filepath = os.path.join(screentshop_path,screent_shot_path,'%s.png' % now)
        self.driver.get_screenshot_as_file(screentshot_filepath)

    def get_title(self):
        title = self.driver.title
        logger.info('获取页面title，title为：%s' % title)
        return title

    def get_alter_text(self):
        self.timeout(2)
        try:
            alter = self.driver.switch_to.alert
            alter_text = alter.text
            logger.info('获取alter弹窗文案，文案为：[%s]' % alter_text)
        except Exception as e:
            logger.error('获取alter弹窗文案失败，原因是：%s' % e)
        return alter_text

if __name__=='__main__':
    pass