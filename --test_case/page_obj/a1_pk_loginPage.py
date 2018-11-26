# coding=utf-8
from public.base import Page

class login(Page):
    """
    User login page
    """
    url = '/admin/auth/login'

    # 输入信息-定位器
    login_username_loc = ('xpath', "//*[@id='cellphone']")
    login_password_loc = ('xpath', "/html/body/div/div/div/div/div/div[2]/form/div[2]/input")
    login_captcha_loc = ('xpath', "//*[@id='myCaptcha']")
    login_button_loc = ('xpath', "/html/body/div/div/div/div/div/div[2]/form/div[4]/button")

    def login_username(self, username):
        self.clear_box(self.login_username_loc, username)
    def login_password(self, password):
        self.input_box(self.login_password_loc, password)
    def login_captcha(self, captcha):
        self.input_box(self.login_captcha_loc, captcha)
    def login_button(self):
        self.click(self.login_button_loc)

    # 登录入口
    def user_login(self, username, password, captcha):
        self.open_url(self.url)
        self.login_username(username)
        self.login_password(password)
        self.login_captcha(captcha)
        self.login_button()

    # 登录结果-定位器
    input_error_loc = ('xpath', "/html/body/div/div/div/div/div/div[2]/div/strong/ul")
    login_succeed_loc = ('xpath', "/html/body/div/header/nav/div/div[1]/a")


    def information_empty(self, anticipant):
        """
        用户信息为空、用户账号输入有误、用户密码输入有误与验证码输入有误等验证
        """
        return self.is_text_in_element(self.input_error_loc, anticipant)

    def login_succeed(self, anticipant):
        """
        登录成功
        """
        self.element_wait_visible(self.login_succeed_loc)
        return self.is_text_in_element(self.login_succeed_loc, anticipant)
