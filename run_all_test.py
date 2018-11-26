#!/usr/bin/python3
# coding=utf-8
from config import globalparam
import HTMLTestReportCN
import time
import unittest

discover = unittest.defaultTestLoader.discover(globalparam.case_path,
                                               pattern=u'test*.py',
                                               top_level_dir=None)


now = time.strftime("%Y_%m_%d")
file_name = globalparam.report_path + '\\' + now + '_UI_automation_result.html'
fp = open(file_name, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title='Brand_card测试报告',
                                         tester=u'QA_AAA',
                                         description='用例执行情况')
runner.run(discover)
fp.close()
