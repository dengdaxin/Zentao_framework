import unittest
from common.basepage import BasePage
from common.browser import Browser
from common.read_config_utils import Config
from common.login_base import LoginBase
from element_infos.login_page import LoginPage
from common.selenium_base import SeleniumBase
from common.element_info_utils import ElementUtils
from common.test_data_utils import TestDataUtils


class LoginCase(SeleniumBase):

    test_class_data = TestDataUtils('login_suite','LoginCase').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_login_success']['isnot'],'跳过执行')
    def test_login_success(self):
        '''登录成功测试'''
        login = LoginBase(self.basepage.driver)
        login.default_login()

    @unittest.skipIf(test_class_data['test_login_fail']['isnot'],'跳过执行')
    def test_login_fail(self):
        '''登录失败测试'''
        test_data = self.test_class_data['test_login_fail']
        login = LoginBase(self.basepage.driver)
        login.login_fail(test_data['test_parameter'].get('username'),test_data['test_parameter'].get('password'))
        alter_text = self.basepage.get_alter_text()
        self.assertEqual(alter_text,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail执行失败')

if __name__=='__main__':
    unittest.main()