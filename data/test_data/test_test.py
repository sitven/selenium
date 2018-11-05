# coding=utf-8
from public.base import Page as pg
from selenium.webdriver.common.by import By
from public.myunit import My_Test
import unittest
import time
class Test_PK(My_Test):
    def test_01(self):
        url = ''
        pg(self.driver).open_url(url)
        time.sleep(3)
        self.input_box(css=(By.ID, 'kw'),text='selenium')
        self.click(css=(By.ID, 'su'))
        print(self.get_title())



if __name__ =="__main__":
    unittest.main()
