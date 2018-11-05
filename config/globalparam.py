# coding=utf-8
from public.readconfig import ReadConfig
import os

# Read configuration file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
# print(config_file_path)

read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# print(read_config)

# Project parameter setting (获取项目绝对路径)
prj_path = os.path.abspath(read_config.getValue("ProjectPath", "project_path"))
# print(prj_path)

# Log path (日志路径)
log_path = os.path.join(prj_path, "report", "logs")
# print(log_path)

# Screenshot file path (截图路径)
img_path = os.path.join(prj_path, "report", "image")
# print(image_path)

# Exception screenshot file path (异常截图路径)
exception_path = os.path.join(prj_path, "report", "expection_image")
# print(exception_path)

# Test report path (测试报告路径)
report_path = os.path.join(prj_path, "report", "test_report")
# print(report_path)

# Upload the autoit file path (上传文件路径)
auto_path = os.path.join(prj_path, " up_files", "autoit_pic")
# print(auto_path)

# Test data path (测试数据路径)
data_path = os.path.join(prj_path, 'data', 'test_data')
#print(data_path)

# Get the browser name (浏览器名称)
browser = read_config.getValue("BrowserType", "browser_name")
# print(browser)

# Get the test url (测试URL)
url = read_config.getValue("testServer", "URL")
# print(url)