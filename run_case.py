import unittest
import os
import time
from BeautifulReport import BeautifulReport
from common.email_utils import EmailUtils
current = os.path.dirname(__file__)
report_path = os.path.join(current,'report/禅道UI自动化测试报告V1.0')
suite = unittest.defaultTestLoader.discover(start_dir='testcase',
                                            pattern='*_case.py',
                                            top_level_dir='testcase')
main_suite = unittest.TestSuite()
main_suite.addTest(suite)
now = time.strftime('%Y_%m_%d_%H_%M_%S')

filename = 'report'+ now
runner = BeautifulReport(main_suite)
runner.report(filename=filename,description='禅道UI自动化测试',report_dir=report_path,theme='theme_default')
