# coding=utf-8
from config.globalparam import data_path
from public.datainfo import ExcelUtil
class Test_Data():
    def a1_data(self, sheet):
       """Get the excel data"""
       filepath = data_path + '\\' + ''
       sheetname = sheet
       data1 = ExcelUtil(filepath, sheetname).dict_data()
       return data1
if __name__ =='__main__':
    data1 = Test_Data().a1_data(sheet='pk_a1_login')
    for x in range(0,5):
        if x == 4:
            print(data1[x]['result'])