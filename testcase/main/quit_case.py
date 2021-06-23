import unittest
from common.quit_base import QuitBase
from common.login_base import LoginBase
from common.selenium_base import SeleniumBase

class QuitCase(SeleniumBase):
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