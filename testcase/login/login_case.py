import unittest
from common.basepage import BasePage
from common.browser import Browser
from common.read_config_utils import Config
from common.login_base import LoginBase
from common.selenium_base import SeleniumBase

class LoginCase(SeleniumBase):
    # def setUp(self) -> None:
    #     self.basepage = BasePage(Browser().get_driver())
    #     self.basepage.open_url(Config.get_config_url)
    #     self.basepage.wait()
    #
    # def tearDown(self) -> None:
    #     self.basepage.quit_browser()

    # def test_login_success(self):
    #     login = LoginBase(self.basepage.driver)
    #     login.login_success('admin','DENGdaxin12')
    def test_login_success(self):
        '''登录成功测试'''
        login = LoginBase(self.basepage.driver)
        login.default_login()

    def test_login_fail(self):
        '''登录失败测试'''
        login = LoginBase(self.basepage.driver)
        login.login_fail('admin','123456')
        alter_text = self.basepage.get_alter_text()
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail执行失败')

if __name__=='__main__':
    unittest.main()