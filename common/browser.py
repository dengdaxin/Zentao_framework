import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.read_config_utils import Config
from common.log_utils import logger
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '..' + Config.get_driver_path)

class Browser():
    def __init__(self,driver_path=driver_path):
        self.driver_path = driver_path

    def get_driver(self,dirver_type=Config.get_driver):
        if dirver_type == 'chrome':
            return  self.__get_chromedriver()
        if dirver_type == 'ie':
            return  self.__get_ie_driver()
        if dirver_type == 'edge':
            return  self.__get_edge_driver()
        if dirver_type == 'firefox':
            return  self.__get_firefox_driver()

    def __get_chromedriver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动化工具的提示
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 取消chrome受自动化工具的提示
        chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
        logger.info('初始化并启动chrome浏览器')
        return driver

    def __get_firefox_driver(self):
        firefoxdriver_path = os.path.join(driver_path,'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefoxdriver_path)
        logger.info('初始化并启动火狐浏览器')
        return driver

    def __get_ie_driver(self):
        iedriver_path = os.path.join(driver_path,'IEDriverServer.exe')
        driver = webdriver.Ie(executable_path=iedriver_path)
        return driver

    def __get_edge_driver(self):
        edgedriver_path = os.path.join(driver_path,'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edgedriver_path)
        return driver

if __name__=='__main__':
    a = Browser(driver_path)
