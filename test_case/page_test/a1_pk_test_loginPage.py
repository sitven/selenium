# coding=utf-8
from public.myunit import My_Test
from public.base import Page
from public import function
from test_case.page_obj.a1_pk_loginPage import login
from data.test_case_data.data_read import Test_Data
import unittest
import ddt

data_error = Test_Data().a1_data(sheet="pk_a1_login")
data_succeed = data_error.pop(4)
logger = 'Login_Test'

@ddt.ddt
class Login_Test(My_Test, unittest.TestCase, Page):
    @ddt.data(*data_error)
    def test_login1_error(self, data, expected=True):
        """用户登录信息错误"""
        po = login(self.driver)
        po.user_login(data['username'], data['password'], data['captcha'])
        self.assert_equal(po.information_empty(data['result']), expected)
        function.insert_img(self.driver, data['screenshot_name'])

    @unittest.skip("跳过此用例")
    def test_login1_success(self, expected=True):
        """登录成功"""
        po = login(self.driver)
        po.user_login(data_succeed['username'], data_succeed['password'], data_succeed['captcha'])
        self.assert_equal(po.login_succeed(data_succeed['result']), expected)
        function.insert_img(self.driver, data_succeed['screenshot_name'])


if __name__ == "__main__":
    unittest.main()