# coding=utf-8
from public.readconfig import ReadConfig
import os

project_path = os.path.split(os.getcwd())[0]
'''Gets the project absolute path (获取项目绝对路径)'''
# print(project_path)

config_file_path = os.path.split(os.path.realpath(__file__))[0]
'''Get the config folder path （获取config文件夹路径）'''
# print(config_file_path)

read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
'''Read configuration file （读取config配置文件）'''
# print(read_config)

log_path = os.path.join(project_path, "report", "logs")
'''write log path (写入的log路径)'''
# print(log_path)

image_path = os.path.join(project_path, "report", "image")
'''The common screenshot path (普通截图路径)'''
# print(image_path)

exception_image_path = os.path.join(project_path, "report", "expection_image")
'''The exception screenshot file path (异常截图路径)'''
# print(exception_image_path)

report_path = os.path.join(project_path, "report", "test_report")
'''Test report path (测试报告路径)'''
# print(report_path)

auto_path = os.path.join(project_path, " up_files", "autoit_pic")
'''Upload the autoit file path (上传文件路径)'''
# print(auto_path)

# Test data path (测试数据路径)
data_path = os.path.join(project_path, 'data', 'test_data')
# print(data_path)

# Get the browser name (浏览器名称)
browser = read_config.getValue("BrowserType", "browser_name")
# print(browser)

url = read_config.getValue("testServer", "URL")
'''Get the test The main domain name (获取测试的主域名)'''
# print(url)