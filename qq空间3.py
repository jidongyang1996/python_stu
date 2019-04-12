#!/user/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
from ddt import ddt, data, unpack
import xlrd


def login(self,u,p):
    self.switch_to.frame('login_frame')
    self.find_element_by_id("u").send_keys(u)
    sleep(1.0)
    self.find_element_by_id('p').send_keys(p)
    sleep(1.0)
    self.find_element_by_class_name('login_button').click()
    sleep(1.0)
    return self.title

class T1(unittest.TestCase):
    def setUp(self):
        dr = webdriver.Chrome()
        dr.get(url='https://qzone.qq.com/')
        dr.implicitly_wait(10.0)
        dr.find_element_by_id('switcher_plogin').click()
        sleep(5.0)
        # dr.switch_to.default_content()

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

    def test_1(self,shuju):
        a = shuju[0].split(',')
        print(a)
        b = a[0]
        c = a[1].strip()
        d = login( b, c)
        self.assertEqual('QQ空间-分享生活，留住感动',)
