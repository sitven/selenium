# coding=utf-8
from config import globalparam
import HTMLTestRunner
import unittest
import time

# test_dir = "./data/test_data"(百度)
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py', top_level_dir=None) (百度)

test_dir = "./test_case/page_test"
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='a1_pk_test*.py', top_level_dir=None)

if __name__ =='__main__':
    # 获取测试开始时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报表储存路径
    file_path = globalparam.report_path + '\\' + now + 'result.html'
    fp = open(file_path, 'wb')

    # 输出测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="PK测试报告", description="用例执行情况:")
    runner.run(discover)
    fp.close()