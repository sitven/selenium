#!/usr/bin/python3
# coding=utf-8

from case.Page_obj.card_01_loginPage import Login
from public.myunit import My_Unit
import unittest
import ddt
from data.login_data import login_user_dict
from data.login_data import login_cookies_dict as cookie_dict
from data.login_data import role_of_login as role

@ddt.ddt
class Login_Test(My_Unit, Login, unittest.TestCase):
    """登录测试类"""
    def test_login_01_username_empty(self):
        """登录—登录账号输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_user_dict[0]['username'],login_user_dict[0]['passwd'],login_user_dict[0]['verify'])
        self.assert_equal(self.po.get_error_text(), login_user_dict[0]['error_message'])

    def test_login_02_passwd_empty(self):
        """登录—登录密码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_user_dict[1]['username'],login_user_dict[1]['passwd'],login_user_dict[1]['verify'])
        self.assert_equal(self.po.get_error_text(), login_user_dict[1]['error_message'])

    def test_login_03_verify_empty(self):
        """登录—登录的验证码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_user_dict[2]['username'],login_user_dict[2]['passwd'],login_user_dict[2]['verify'])
        self.assert_equal(self.po.get_error_text(), login_user_dict[2]['error_message'])

    def test_login_04_userpasswd_error(self):
        """登录—登录验证码错误"""
        self.po = Login(self.driver)
        self.po.login_process(login_user_dict[3]['username'],login_user_dict[3]['passwd'],login_user_dict[3]['verify'])
        self.assert_equal(self.po.get_error_text(), login_user_dict[3]['error_message'])

    @unittest.skip('跳过数据驱动测试用例')
    @ddt.data(*login_user_dict)
    def test_login_05_ddt(self, data):
        """数据驱动测试--ddt"""
        self.po = Login(self.driver)
        self.po.login_process(data['username'], data['passwd'], data['verify'])
        self.assert_equal(self.get_error_text(), data['error_message'])

    def test_login_06_cookies(self):
        """通过cookies绕过登录"""
        self.po = Login(self.driver)
        self.po.cookie_login(cookie_dict)
        self.assertEqual(self.po.get_role_text(), role[0])


if __name__ == "__main__":
    unittest.main()