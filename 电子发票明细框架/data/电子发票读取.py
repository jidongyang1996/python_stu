#!/user/bin/python
# -*- coding:utf-8 -*-
import xlrd
class fapiaoduqu(object):
    def dqjcsj(self):
        shuju=[]
        f = xlrd.open_workbook(r'E:\python学习\电子发票明细框架\data\发票.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__=='__main__':
    print(fapiaoduqu().dqjcsj())
