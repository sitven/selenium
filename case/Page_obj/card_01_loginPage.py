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
        self.open_url(self.url)
        self.login_username(username)
        self.login_passwd(passwd)
        self.login_verify(verify)
        self.login_button()

    # 登录结果
    login_hint_loc = ('xpath', "//div[@class='tips']")                          # 失败提示
    login_succee_loc = ('xpath', "//button[@class='btn btn-blueframe']")        # 成功标题

    # 获取失败文案
    def get_fial_text(self):
        return self.get_text(self.login_hint_loc)

    # 获取成功页面微信查看按钮文案
    def get_succees_text(self):
        return self.get_text(self.login_succee_loc)