#!/user/bin/python
# -*- coding:utf-8 -*-
import xlrd
def duqu():
    shuju = []
    f = xlrd.open_workbook(r'E:\python学习\qq空间测试\data\zhma.xlsx')
    sheet = f.sheets()[1]
    num = sheet.nrows
    for i in range(1,num):
        shuju.append(sheet.row_values(i))
    return shuju


if __name__ == '__main__':
    print(duqu())