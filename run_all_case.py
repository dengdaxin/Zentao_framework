import os
import unittest
import time
import sys
from demo.email_ut import seamil
from common import HTMLTestReportCN
from common.email_utils import EmailUtils

current = os.path.dirname(__file__)
report_path = os.path.join(current,'report/')
case_path= os.path.join(current,'testcase')

class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = 'UI自动化测试'
        self.description = '描述描述描述'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir = self.test_case_path,
                                                       pattern='*_case.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='dengdaxin')
        runner.run(all_suite)
        fp.close()
        return report_path

if __name__ == '__main__':
    report_path = RunAllCases().run()
    #seamil(report_path, 'test_report%s.html' % time.strftime('%Y_%m_%d_%H_%M_%S'))  # 把测试结果做为附件发发送
    #EmailUtils('<h3 align="center">禅道自动化测试报告</h3>',report_path).send_mail()








