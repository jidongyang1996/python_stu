#!/user/bin/python
# -*- coding:utf-8 -*-
import xlrd
class suopeiduqu(object):
    def duqu_jichushuju(self):
        shuju=[]
        f=xlrd.open_workbook(r'E:\python学习\框架\data\suopei.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
            if i==0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
if __name__=='__main__':
    suopeiduqu().duqu_jichushuju()
