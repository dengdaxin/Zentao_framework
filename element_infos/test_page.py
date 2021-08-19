# --coding:utf-8--
import time
from common.basepage import BasePage
from common.login_base import LoginBase
from element_infos.login_page import LoginPage
from common.element_info_utils import ElementUtils
from common.browser import Browser
from common.read_config_utils import Config

class TestPage(LoginPage):
    def __init__(self,driver):
        super().__init__(driver=driver)
        element = ElementUtils('test_suite','test').get_elements_info()
        self.test_module = element['test_module']
        self.bug_module = element['bug_module']
        self.create_bug = element['create_bug']
        self.product_chosen_0 = element['product_chosen']
        self.product_chosen_1 = element['click_product_chosen']
        self.module_chosen_0 = element['module_chosen']
        self.module_chosen_1 = element['click_module_chosen']
        self.project_chosen_0 = element['project_chosen']
        self.project_chosen_1 = element['click_project_chosen']
        self.openedBuild_chosen_0 = element['openedBuild_chosen']
        self.openedBuild_chosen_1 = element['click_openedBuild_chosen']
        self.assignedTo_chosen_0 = element['assignedTo_chosen']
        self.assignedTo_chosen_1 = element['click_assignedTo_chosen']
        self.deadline_0 = element['deadline']
        self.type_chosen_0 = element['type_chosen']
        self.type_chosen_1 = element['click_type_chosen']
        self.os_chosen_0 = element['os_chosen']
        self.os_chosen_1 = element['click_os_chosen']
        self.browser_chosen_0 = element['browser_chosen']
        self.browser_chosen_1 = element['click_browser_chosen']
        self.input_bug_title_0 = element['input_bug_title']
        self.severity_0 = element['severity']
        self.severity_1 = element['click_severity']
        self.pri_0 = element['pri']
        self.pri_1 = element['click_pri']
        self.claer_article_content_0 = element['claer_article_content']
        self.input_article_content_0 = element['input_article_content']
        self.click_submit = element['submit']
        self.iframe_0 = element['iframe']


    def click_test_module(self):
        '''点击测试模块'''
        self.click(self.test_module)

    def click_bug(self):
        '''点击bug'''
        self.click(self.bug_module)

    def click_bug_create(self):
        '''提bug按钮'''
        self.click(self.create_bug)

    def product_chosen(self):
        '''所属产品'''
        self.click(self.product_chosen_0)

    def click_product_chosen(self):
        '''选择所属产品'''
        self.click(self.product_chosen_1)

    def module_chosen(self):
        '''所属模块'''
        self.click(self.module_chosen_0)

    def click_module_chosen(self):
        '''选择所属模块'''
        self.click(self.module_chosen_1)

    def project_chosen(self):
        '''所属项目'''
        self.click(self.project_chosen_0)

    def click_project_chosen(self):
        '''选择所属项目'''
        self.click(self.project_chosen_1)
        self.timeout(2)

    def openedBuild_chosen(self):
        '''影响版本'''

        self.click(self.openedBuild_chosen_0)

    def click_openedBuild_chosen(self):
        '''选择影响版本'''

        self.click(self.openedBuild_chosen_1)

    def assignedTo_chosen(self):
        '''当前指派'''
        self.click(self.assignedTo_chosen_0)

    def click_assignedTo_chosen(self):
        '''选择当前指派人'''
        self.click(self.assignedTo_chosen_1)
        self.timeout(2)

    def deadline(self,datatime):
        '''截止日期'''
        self.input(self.deadline_0,datatime)

    def type_chosen(self):
        '''bug类型'''
        self.click(self.type_chosen_0)

    def click_type_chosen(self):
        '''选择bug类型'''
        self.click(self.type_chosen_1)


    def os_chosen(self):
        '''操作系统'''
        self.click(self.os_chosen_0)

    def click_os_chosen(self):
        '''选择操作系统'''
        self.click(self.os_chosen_1)

    def browser_chosen(self):
        '''浏览器'''
        self.click(self.browser_chosen_0)

    def click_browser_chosen(self):
        '''选择浏览器'''
        self.click(self.browser_chosen_1)

    def input_bug_title(self,title):
        '''bug标题'''
        self.input(self.input_bug_title_0,title)

    def severity(self):
        '''严重程度'''
        self.click(self.severity_0)

    def click_severity(self):
        '''选择严重程度'''
        self.click(self.severity_1)

    def pri(self):
        '''优先级'''
        self.click(self.pri_0)

    def click_pri(self):
        '''选择优先级'''
        self.click(self.pri_1)

    def claer_article_content(self):
        '''清空重现步骤'''
        self.clear(self.claer_article_content_0)

    def input_article_content(self,content):
        '''输入重现步骤'''
        self.input(self.input_article_content_0,content)

    def submit(self):
        '''提交bug表单'''
        self.click(self.click_submit)

    def switch_to_iframe(self):
        self.switch_iframe(self.iframe_0)


if __name__=='__main__':
    driver = Browser().get_driver()
    test = TestPage(driver)
    test.open_url(Config.get_config_url)
    test.max_browser()
    test.input_username('test01')
    test.input_password('newdream123')
    test.click_login()
    time.sleep(2)
    test.click_test_module()
    test.click_bug()
    test.click_bug_create()
    test.product_chosen()
    test.click_product_chosen()
    test.module_chosen()
    test.click_module_chosen()
    test.project_chosen()
    test.click_project_chosen()

    test.openedBuild_chosen()
    test.click_openedBuild_chosen()
    test.assignedTo_chosen()
    test.click_assignedTo_chosen()
    test.deadline('2021-08-30')
    test.type_chosen()
    test.click_type_chosen()
    test.os_chosen()
    test.click_os_chosen()
    test.browser_chosen()
    test.click_browser_chosen()
    test.input_bug_title('222222222')
    test.severity()
    test.click_severity()
    test.pri()
    test.click_pri()
    test.switch_iframe(test.iframe_0)
    test.claer_article_content()
    test.input_article_content('sssssssss')
    test.exit_iframe()
    test.submit()

