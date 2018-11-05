# coding=utf-8
class Baidu_Module():
    def __init__(self,driver):
        self.dr = driver
    def login(self,values):
        login_dr = self.dr
        login_dr.get("https://www.baidu.com")
        login_dr.find_element_by_id('kw').send_keys(values)
        login_dr.find_element_by_id('su').click()

    def login_out(self):
        self.dr.quit()