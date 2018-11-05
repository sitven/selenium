# coding=utf-8
from selenium import webdriver

def select_browser(browser='Ie'):
    if browser == 'Chrome' or browser == "Ch":
        dr = webdriver.Chrome()
    if browser == 'Firefox' or browser == 'Ff':
        dr = webdriver.Firefox()
    if browser == 'Ie' or browser == 'ie':
        dr = webdriver.Ie
    return dr