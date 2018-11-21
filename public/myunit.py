# coding=utf-8
from public.log import Logger
from public.browser import select_browser
from config import globalparam
from public.base import Page
import unittest

class My_Test(unittest.TestCase, Page):
    @classmethod
    def setUpClass(self):
        self.logger = Logger()
        print('A')
        self.logger.info('############################### START ###############################')
        print('B')
        self.driver = select_browser(globalparam.browser)
        print('C')
        Page(self.driver).max_window()
        Page(self.driver).wait(secs=2)

    @classmethod
    def tearDownClass(self):
        Page(self.driver).quit_browser()
        self.logger.info('###############################  END  ###############################')

