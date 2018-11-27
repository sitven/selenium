#!/usr/bin/python3
# coding=utf-8

from selenium import webdriver
from data.login_data import login_cookies
import time


driver = webdriver.Chrome()
driver.get("https://pre-pcauto.pangku.com/dist/index.html")
driver.maximize_window()
driver.add_cookie(login_cookies)
time.sleep(1)
driver.get("https://pre-pcauto.pangku.com/dist/index.html#/Setcard/")
time.sleep(1)
text = driver.find_element_by_xpath("//button[@class='btn']").text
print(text)
print(driver.title)
driver.quit()