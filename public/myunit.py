# coding=utf-8
from public.browser import select_browser
from config.globalparam import browser
from public.base import Page
import unittest
from public.log import My_Log

class My_Unit(unittest.TestCase, My_Log):
    @classmethod
    # def setUpClass(self):
    #     # My_Log().info('############################### START ###############################')
    #     self.driver = select_browser(browser)
    #     Page(self.driver).max_window()
    #     Page(self.driver).wait(secs=2)
    #
    # @classmethod
    # def tearDownClass(self):
    #     Page(self.driver).quit_browser()
    #     My_Log().info('###############################  END  ###############################')

    def test_unit_01(self):
        My_Log().info('############################### START ###############################')
        self.driver = select_browser(browser)
        Page(self.driver).max_window()
        Page(self.driver).wait(secs=2)

    def test_unit_02(self):
        Page(self.driver).quit_browser()
        My_Log().info('###############################  END  ###############################')

