#!/usr/bin/python3
# coding=utf-8

# 登录数据
login_user_dict = [{'case_name':'登录账号为空', 'username':'', 'passwd':'password', 'verify':'a12fd',
                    'error_message':'请输入账号'},
                   {'case_name':'登录密码为空', 'username':'username', 'passwd':'', 'verify':'a12fd',
                    'error_message': '请输入密码'},
                   {'case_name':'登录验证码为空', 'username':'username', 'passwd':'password', 'verify':'',
                    'error_message': '请输入验证码'},
                   {'case_name':'登录验证码输入错误', 'username':'username', 'passwd':'password', 'verify':'12345',
                    'error_message':'验证码错误，请输入正确的验证码'}]
# 登录cookie
login_cookies_dict = {'expiry': 1543887494, 'name': 'b_login',
                      'value': 'eyJpdiI6Ikd5V1U3dnNqa2crd2hFdDExeFpmblE9PSIsInZhbHVlIjoiSGxYWFZHeHVUZHhaM25tZkNi'
                               'cHN6UGYzRlRyXC9FS2Rxdjgrc3YzMnVQK1BhVSt6WDJ0TW1mNDNJUzNLZm1zcXkiLCJtYWMiOiJjOTExZ'
                               'jUwZDg0NjU3ZjFkNGM2NDRmNzJkM2U3MTYwYTA4MjY0OTI5MDI2ZGJiMTNiNjk3MDg4ZGZmYjNkMTYzIn0%3D'}

# 角色信息
role_of_login = ['管理员', '普通用户']
