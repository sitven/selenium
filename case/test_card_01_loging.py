#!/usr/bin/python3
# coding=utf-8

from case.Page_obj.card_01_loginPage import Login
from public.myunit import My_Unit
import unittest
import ddt
from data.test_case_data.data import login_test_data as login_data

@ddt.ddt
class Login_Test(My_Unit, Login, unittest.TestCase):

    @unittest.skip('跳过用例:test_login_01_username_empty')
    def test_login_01_username_empty(self):
        """用户登录-用户名输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_data[0]['username'], login_data[0]['passwd'], login_data[0]['verify'])
        self.assert_equal(self.po.get_fial_text(), login_data[0]['assert'])

    @unittest.skip('跳过用例:test_login_01_passwd_empty')
    def test_login_02_passwd_empty(self):
        """用户登录-密码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_data[1]['username'], login_data[1]['passwd'], login_data[1]['verify'])
        self.assert_equal(self.po.get_fial_text(),login_data[1]['assert'])

    @unittest.skip('跳过用例:test_login_03_verify_empty')
    def test_login_03_verify_empty(self, login_data):
        """用户登录-验证码输入为空"""
        self.po = Login(self.driver)
        self.po.login_process(login_data[2]['username'], login_data[2]['passwd'], login_data[2]['verify'])
        self.assert_equal(self.get_fial_text(), login_data[2]['assert'])

    @ddt.data(*login_data)
    def test_login_ddt(self, data):
        """数据驱动测试--ddt"""
        self.po = Login(self.driver)
        self.po.login_process(data['username'], data['passwd'], data['verify'])
        self.assert_equal(self.get_fial_text(), data['assert'])

    def test_login_04(self):
        """通过cookies登录"""
if __name__ == "__main__":
    unittest.main()