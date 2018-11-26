#!/usr/bin/python3
# coding=utf-8

# 登录数据
login_test_data = [{'case_name':'登录账号为空', 'username':'', 'passwd':'password', 'verify':'a12fd',
                    'assert':'请输入账号'},
                   {'case_name':'登录密码为空', 'username':'username', 'passwd':'', 'verify':'a12fd',
                    'assert': '请输入密码'},
                   {'case_name':'登录验证码为空', 'username':'username', 'passwd':'password', 'verify':'',
                    'assert': '请输入验证码'},
                   {'case_name':'登录验证码错误', 'username':'username', 'passwd':'password', 'verify':'12345',
                   'assert':'验证码错误，请输入正确的验证码'}]
