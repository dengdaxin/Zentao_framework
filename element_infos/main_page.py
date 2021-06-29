from common.element_info_utils import ElementUtils
from common.basepage import BasePage
from common.browser import Browser
from common.login_base import LoginBase
from common.read_config_utils import Config
class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element = ElementUtils('main_suite','main').get_elements_info()
        self.bug_menu_click = element['bug_click']
        self.user_info = element['user_info']
        self.quit_login = element['quit_login']

    def bug_menu(self):
        self.click(self.bug_menu_click)

    def user_info_click(self):
        self.click(self.user_info)

    def quit_login_click(self):
        self.click(self.quit_login)

if __name__=='__main__':
    driver = Browser().get_driver()
    driver.get(Config.get_config_url)
    main = LoginBase(driver).default_login()
    m = MainPage(driver)
    m.timeout(2)
    m.user_info_click()
    m.quit_login_click()