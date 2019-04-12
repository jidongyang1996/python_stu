#!/user/bin/python
# -*- coding:utf-8 -*-
# from selenium import webdriver
# import unittest
# import xlrd
# from time import sleep
# class qqkj(unittest.TestCase):
#     def llq(self):
#         self.dr=webdriver.Chrome()
#     def gb(self):
#         self.dr.quit()
#     def test_1(self):
#         a=xlrd.open_workbook(r'E:\python学习\qq空间测试\data\zhma.xlsx')
#         sheet=a.sheets()[0]
#         b=sheet.nrows
#         for i in range(1,b):
#             self.dr.get('https://qzone.qq.com/')
#             name=

from selenium import webdriver
from time import sleep
import unittest
from ddt import ddt, data, unpack
import xlrd

def login(dr, u, p):
    dr.find_element_by_id('switcher_plogin').click()
    sleep(5.0)
    dr.switch_to.default_content()
    dr.switch_to_frame('login_frame')
    dr.find_element_by_id("u").send_keys(u)
    sleep(1.0)
    dr.find_element_by_id('p').send_keys(p)
    sleep(1.0)
    dr.find_element_by_class_name('login_button').click()
    sleep(1.0)
    return dr.title


@ddt  # 固定写法
class T1(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get(url='https://qzone.qq.com/')
        self.dr.implicitly_wait(10.0)
        self.dr.switch_to.frame('login_frame')
    def dq(self):
            shuju = []
            f = xlrd.open_workbook(r'E:\python学习\电子发票明细框架\data\发票.xlsx')
            sheet = f.sheets()[0]
            num = sheet.nrows
            for i in range(num):
                if i == 0:
                    continue
                else:
                    shuju.append(sheet.row_values(i))
            return shuju

    @data(dq(self))
    def test_2(self,shuju):
        a = shuju[0].split(',')
        print(a)
        b = a[0]
        c = a[1].strip()
        d = login(self.dr, b, c)
        self.assertEqual('QQ空间-分享生活，留住感动',self.dr.title)
        print(self.dr.title)

    def tearDown(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()
