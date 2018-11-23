#!/usr/bin/python35
# coding=utf-8

from public.base import Page

class Login(Page):
    ''' 账户登录测试 '''

    # 子域名
    url = '/dist/index.html'

    # 定位器
    login_username_loc = ('xpath', "//input[@autofocus='autofocus']")       # 账号
    login_passwd_loc = ('xpath', "//input[@type='password']")               # 密码
    login_verify_loc = ('xpath', "//input[@class='small']")                 # 验证码
    login_button_loc = ('xpath', "//button[@class='uc_submit_ok']")         # 登录

    def login_username(self, username):
        self.input_box(self.login_username_loc, username)

    def login_passwd(self, passwd):
        self.input_box(self.login_passwd_loc, passwd)

    def login_verify(self,verify):
        self.input_box(self.login_verify_loc, verify)

    def login_button(self):
        self.click(self.login_button_loc)

    def login_get_error(self):
        self.get_text(self.login_hint_loc)

    # 登录流程
    def login_process(self, username, passwd, verify):
        print(1)
        self.open_url(self.url)
        print(2)
        self.login_username(username)
        print(3)
        self.login_passwd(passwd)
        print(4)
        self.login_verify(verify)
        print(5)
        self.login_button()
        print(6)

    # 登录结果
    login_hint_loc = ('xpath', "//div[@class='tips']")                          # 失败提示
    login_succee_loc = ('xpath', "//button[@class='btn btn-blueframe']")        # 成功标题

    # 获取失败文案
    def get_fial_text(self):
        return self.get_text(self.login_hint_loc)

    # 获取成功页面微信查看按钮文案
    def get_succees_text(self):
        return self.get_text(self.login_succee_loc)





#
# if __name__ == "__main__":
#     from selenium import webdriver
#     import time
#     driver = webdriver.Chrome()
#     driver.get("https://pre-pcauto.pangku.com/dist/index.html")
#     driver.find_element_by_xpath("//input[@autofocus= 'autofocus']").send_keys('admin')
#     driver.find_element_by_xpath("//input[@type='password']").send_keys('admin2018')
#     driver.find_element_by_xpath("//input[@class='small']").send_keys('dddfff')
#     time.sleep(5)
#     driver.find_element_by_xpath("//button[@class='uc_submit_ok']").click()
#     time.sleep(2)
#     text = driver.find_element_by_xpath("//div[@class='tips']").text
#     print(text)
#     print(driver.title)
#     driver.quit()
