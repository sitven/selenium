#!/usr/bin/python3
# coding=utf-8

login_test_data = [{'case_name':'登录账号为空', 'username':'', 'passwd':'password', 'verify':'a12fd'},
                   {'case_name':'登录密码为空', 'username':'username', 'passwd':'', 'verify':'a12fd'},
                   {'case_name':'登录验证码为空', 'username':'username', 'passwd':'password', 'verify':''},
                   {'case_name':'登录账号密码erro', 'username':'username', 'passwd':'password', 'verify':'12345'}]

print(login_test_data[0]['case_name'])
