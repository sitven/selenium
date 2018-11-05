# coding=utf-8
import xlrd

class ExcelUtil():
    """获取xls或者xlsx文件里的数据并返回字典组成的列表"""
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)                    # 打开配置文件
        self.table = self.data.sheet_by_name(sheetName)              # 获取配置数据表名
        self.keys = self.table.row_values(0)                         # 获取表首行为key
        self.rowNum = self.table.nrows                               # 获取总行数
        self.colNum = self.table.ncols                               # 获取总列数
    def dict_data(self):
        if self.rowNum < 2:
            print("表中数据小于2行，请添加测试数据")
        else:
            userinfo = []
            num = 1
            for i in range(self.rowNum - 1):
                user = {}
                # 从第二行开始取value值
                values = self.table.row_values(num)
                for x in range(self.colNum):
                    user[self.keys[x]] = values[x]
                userinfo.append(user)
                num += 1
            return userinfo

if __name__ == '__main__':
    excelPath = "E:\\GitHub\\data\\test_data\\datas.xlsx"
    sheetName = 'a1_sta'
    data = ExcelUtil(excelPath, sheetName)
    print(data.dict_data())


