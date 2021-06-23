from common.basepage import BasePage
#from element_infos.main_page import MainPage
from element_infos.login_page import LoginPage
from common.read_config_utils import Config
class LoginBase:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    def login_success(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def default_login(self):
        self.login_success(username=Config.get_username,password=Config.get_password)
        #return MainPage(self.login_page.driver)

    def login_fail(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()