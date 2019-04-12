#!/user/bin/python
# -*- coding:utf-8 -*-
import xlrd
class zhmaduqu(object):
    def dqsj(self):
        shuju=[]
        f = xlrd.open_workbook(r'E:\python学习\qq空间测试\data\zhma.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__=='__main__':
    print(zhmaduqu().dqsj())