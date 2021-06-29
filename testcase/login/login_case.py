import unittest
from common.basepage import BasePage
from common.browser import Browser
from common.read_config_utils import Config
from common.login_base import LoginBase
from common.selenium_base import SeleniumBase
from common.element_info_utils import ElementUtils
import t

class LoginCase(SeleniumBase):

    success = t.get_isnot('login','username_input')
    fail = t.get_isnot('login','password_input')

    @unittest.skipIf(True if success == '是' else False,'跳过执行')
    def test_login_success(self):
        '''登录成功测试'''
        login = LoginBase(self.basepage.driver)
        login.default_login()

    @unittest.skipIf(True if fail == '是' else False,'跳过执行')
    def test_login_fail(self):
        '''登录失败测试'''
        login = LoginBase(self.basepage.driver)
        login.login_fail('admin','123456')
        alter_text = self.basepage.get_alter_text()
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail执行失败')

if __name__=='__main__':
    unittest.main()