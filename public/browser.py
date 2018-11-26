#!/usr/bin/python3
# coding=utf-8
from selenium import webdriver
def select_browser(browser):
    dr = None
    if browser == 'Chrome' or browser == "Ch":
        dr = webdriver.Chrome()
    elif browser == 'Firefox' or browser == 'Ff':
        dr = webdriver.Firefox()
    elif browser == 'Ie' or browser == 'ie':
        dr = webdriver.Ie
    return dr