#!/usr/bin/python3
# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
print(driver.title)
driver.quit()