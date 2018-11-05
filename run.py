#!/usr/bin/python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")
eles = driver.find_elements_by_xpath("//*[@id='u1']/a")
print(eles)
time.sleep(2)
driver.quit()
# (By.xpath("//div[contains(text(),'modifyFilterTest002')]"))