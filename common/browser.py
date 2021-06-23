import os
from selenium import webdriver
from common.read_config_utils import Config
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '..' + Config.get_driver_path)

class Browser():
    def __init__(self,driver_path=driver_path):
        self.driver_path = driver_path

    def get_driver(self,dirver_type=Config.get_driver):
        if dirver_type == 'chrome':
            return  self.__get_chromedriver()

    def __get_chromedriver(self):
        chromedriver_path = os.path.join(driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        return driver

    def __get_iedriver(self):
        pass

    def __get_edge_driver(self):
        pass

if __name__=='__main__':
    a = Browser(driver_path)
