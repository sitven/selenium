#!/usr/bin/python3
# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
WebDriverWait(driver, 5).until(EC.visibility_of(driver.find_element(by=By.ID,value='kw')), message='元素kw未出现')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
print(driver.title)
driver.quit()