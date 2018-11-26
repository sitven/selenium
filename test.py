#!/usr/bin/python3
# coding=utf-8
from data.test_case_data.data import login_test_data
import ddt
import unittest

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("\n setUp stard")

    def tearDown(self):
        print("tearDown end \n")

    # def setUpClass(cls):
    #     print("setUpclass stard")
    #
    # def tearDownClass(cls):
    #     print("tearDownclass end")

    @ddt.data(*login_test_data)
    def test_o1(self, data):
        print(data)
