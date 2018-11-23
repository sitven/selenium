#!/usr/bin/python3
# coding=utf-8

# def test_baidu():
#     from selenium import webdriver
#     import time
#     from selenium.webdriver.support import expected_conditions as EC
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.wait import WebDriverWait
#
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     WebDriverWait(driver, 5).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')), message='元素kw未出现')
#     driver.find_element_by_id('kw').send_keys('selenium')
#     driver.find_element_by_id('su').click()
#     time.sleep(3)
#     print(driver.title)
#     driver.quit()


# import logging
# import os
# log_name = os.path.join(os.getcwd(), 'report\logs', 'run_test.log')
#
# logging.basicConfig(format='[%(asctime)s] [%(pathname)s[line:%(lineno)d]] [%(levelname)s] [%(message)s]',
#                     filename=log_name,
#                     filemode='a',
#                     level=logging.DEBUG)
#
# logging.debug('is debug')
# logging.info('is info')
# logging.warning('is warning')
# logging.error('is error')
# logging.critical('is critical')

from selenium import webdriver
from public.log import My_Log
import time
log = My_Log()

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
log.info(message='百度输入框输入selenium')
driver.find_element_by_id('su').click()
log.info(message='点击百度一下')
time.sleep(3)
driver.quit()