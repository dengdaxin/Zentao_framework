# --coding:utf-8--
import unittest
from common.login_base import LoginBase
from common.selenium_base import SeleniumBase
from common.test_data_utils import TestDataUtils
from element_infos.test_page import TestPage
class CreateBugCase(SeleniumBase):
    test_class_data = TestDataUtils('test_suite','CreateBugCase').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_create_bug']['isnot'], '跳过执行')
    def test_create_bug(self):
        '''创建bug测试'''
        test_data = self.test_class_data['test_create_bug']
        login = LoginBase(self.basepage.driver)
        login.default_login()
        test = TestPage(self.basepage.driver)
        test.click_test_module()
        test.click_bug()
        test.click_bug_create()
        test.product_chosen()
        test.click_product_chosen()
        test.module_chosen()
        test.click_module_chosen()
        test.project_chosen()
        test.click_project_chosen()
        test.openedBuild_chosen()
        test.click_openedBuild_chosen()
        test.assignedTo_chosen()
        test.click_assignedTo_chosen()
        test.deadline(test_data['test_parameter'].get('datatime'))
        test.type_chosen()
        test.click_type_chosen()
        test.os_chosen()
        test.click_os_chosen()
        test.browser_chosen()
        test.click_browser_chosen()
        test.input_bug_title(test_data['test_parameter'].get('title'))
        test.severity()
        test.click_severity()
        test.pri()
        test.click_pri()
        test.switch_to_iframe()
        test.claer_article_content()
        test.input_article_content(test_data['test_parameter'].get('content'))
        test.exit_iframe()
        test.execute_script()
        test.submit()

if __name__=='__main__':
    unittest.main()