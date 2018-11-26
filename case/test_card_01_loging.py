#!/usr/bin/python3
# coding=utf-8

from case.Page_obj.card_01_loginPage import Login
from public.myunit import My_Unit
import unittest
import ddt
from data.test_case_data.data import login_test_data as data

class Login_Test(My_Unit, Login, unittest.TestCase):

    def test_login_01_username_empty(self):
        """用户登录-用户名输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(data[0]['username'], data[0]['passwd'], data[0]['verify'])
        self.assert_equal(self.po.get_fial_text(), '请输入账号')

    def test_login_02_passwd_empty(self):
        """用户登录-密码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(data[1]['username'], data[1]['passwd'], data[1]['verify'])
        self.assert_equal(self.po.get_fial_text(), '请输入密码')

    def test_login_03_verify(self):
        """用户登录-验证码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(data[2]['username'], data[2]['passwd'], data[2]['verify'])
        self.assert_equal(self.get_fial_text(), '请输入验证码')


if __name__ == "__main__":
    Login_Test().test_login_01_username_empty()
    Login_Test().test_login_02_passwd_empty()
    Login_Test().test_login_03_verify()