from common.login_base import LoginBase
import time
from common.selenium_base import SeleniumBase
from selenium import webdriver
from common.read_config_utils import Config
driver = webdriver.Chrome()
driver.get(Config.get_config_url)
LoginBase(driver).login_fail('admin','DENGdaxin12')
time.sleep(1)
# 获取alert对话框
alert = driver.switch_to.alert
time.sleep(1)
# 打印警告对话框内容
print(alert.text)
time.sleep(3)
alert.accept()