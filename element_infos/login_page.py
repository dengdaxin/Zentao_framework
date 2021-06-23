import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.read_config_utils import Config
from common.basepage import BasePage
from common.element_info_utils import ElementUtils
from common.browser import Browser

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        element = ElementUtils('login').get_elements_info()
        self.username_input = element['username_input']
        self.password_input = element['password_input']
        self.click_login_button = element['login_click']

    def input_username(self,username):
        self.input(self.username_input,username)

    def input_password(self, password):
        self.input(self.password_input,password)

    def click_login(self):
        self.click(self.click_login_button)


if __name__=='__main__':
    driver = Browser().get_driver()
    login = LoginPage(driver)
    login.open_url(Config.get_config_url)
    login.input_username('admin')
    login.input_password('DENGdaxin12')
    login.click_login()
