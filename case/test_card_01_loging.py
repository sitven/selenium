#!/usr/bin/python3
# coding=utf-8

from case.Page_obj.card_01_loginPage import Login
from public.myunit import My_Unit
import unittest

class Login_Test(My_Unit, Login, unittest.TestCase):
    def test_login_01_username_empty(self):
        """用户登录-用户名输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(username='', passwd='password', verify='12345')
        self.assert_equal(self.po.get_fial_text(), '请输入账号')

    def test_login_02_passwd_empty(self):
        """用户登录-密码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(username='user', passwd='', verify='12345')
        self.assert_equal(self.po.get_fial_text(), '请输入密码')

    def test_login_03_verify(self):
        """用户登录-验证码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(username='user', passwd='password', verify='')
        self.assert_equal(self.get_fial_text(), '请输入验证码')


if __name__ == "__main__":
    Login_Test().test_login_01_username_empty()
    Login_Test().test_login_02_passwd_empty()
    Login_Test().test_login_03_verify()