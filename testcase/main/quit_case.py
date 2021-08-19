import unittest
from common.quit_base import QuitBase
from common.login_base import LoginBase
from common.selenium_base import SeleniumBase
from common.test_data_utils import TestDataUtils

class QuitCase(SeleniumBase):
    test_class_data = TestDataUtils('main_suite', 'QuitCase').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_quit']['isnot'],'跳过执行')
    def test_quit(self):
        '''退出登录测试'''
        login = LoginBase(self.basepage.driver)
        login.default_login()
        quit = QuitBase(self.basepage.driver)
        action = quit.quit()
        value = action.get_title()
        self.assertEqual(value,'用户登录 - 禅道','test_quit用例执行失败')

if __name__=='__main__':
    unittest.main()