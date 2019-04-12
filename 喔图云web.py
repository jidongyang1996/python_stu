#!/user/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from ddt import ddt,file_data,data,unpack
import unittest
import xlrd
def qq(argument,u,p):
    argument.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
    argument.find_element_by_xpath('/html/body/div/div/div[2]/div/section[2]/div/input').send_keys('u')
    sleep(2)
    argument.find_element_by_xpath('/html/body/div/div/div[2]/div/section[3]/div/input').send_keys('p')
    sleep(2)
    argument.find_element_by_xpath('/html/body/div/div/div[2]/div/section[4]/div').click()
    return argument.title
# @ddt
# class wt(unittest.TestCase):
#     @classmethod
#     def setUp(self):
#         self.dr=webdriver.Chrome()
#         self.dr.get('https://www.alltuu.com/')
#         self.dr.implicitly_wait(10.0)
#
#     @file_data(r'E:\python学习\ceshi\jianshu\data\login.json')
#     # @file_data(r'E:\python学习\电子发票明细框架\data\fafa.xlsx')
#     def test_2(self,value):
#         print(value)
#         a=value[0].split(',')
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d = qq(self.dr, b, c)
#         print(d)
#
#     @classmethod
#     def tearDown(self):
#         self.dr.quit()
# if __name__=='__main__':
#     unittest.main()



# def dq():
#         shuju = []
#         f = xlrd.open_workbook(r'E:\python学习\电子发票明细框架\data\发票.xlsx')
#         sheet = f.sheets()[0]
#         num = sheet.nrows
#         for i in range(num):
#             if i == 0:
#                 continue
#             else:
#                 shuju.append(sheet.row_values(i))
#         return shuju
# def test_1(value):
#     for i in value:
#         print(i)
#         a=i[0]
#         print(a)
#         b=i[1]
#         dr=webdriver.Chrome()
#         dr.get('https://www.alltuu.com/')
#         dr.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
#         dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[2]/div/input').send_keys(a)
#         sleep(2)
#         dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[3]/div/input').send_keys(b)
#         sleep(2)
#         dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[4]/div').click()
#
#
# a=dq()
# test_1(a)




# from selenium import webdriver
# from time import sleep
# import unittest
# from ddt import ddt, data, unpack
#
#
# def login(argument, u, p):
#     argument.find_element_by_id('switcher_plogin').click()
#     sleep(5.0)
#     argument.switch_to.default_content()
#     argument.switch_to_frame('login_frame')
#     argument.find_element_by_id("u").send_keys(u)
#     sleep(1.0)
#     argument.find_element_by_id('p').send_keys(p)
#     sleep(1.0)
#     argument.find_element_by_class_name('login_button').click()
#     sleep(1.0)
#     return argument.title
#
#
# @ddt  # 固定写法
# class T1(unittest.TestCase):
#     #
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Chrome()
#         cls.dr.get(url='https://qzone.qq.com/')
#         cls.dr.implicitly_wait(10.0)
#         cls.dr.switch_to_frame('login_frame')
#
#     # def test_1(self):
#     #     dr.implicitly_wait(10.0)
#     #     dr.switch_to_frame('login_frame')
#     #     dr.find_element_by_id('switcher_plogin').click()
#     #     sleep(5.0)
#     #     dr.switch_to.default_content()
#     #     dr.switch_to_frame('login_frame')
#     #     dr.find_element_by_id("u").send_keys('825069672')
#     #     sleep(1.0)
#     #     dr.find_element_by_id('p').send_keys('houec1019')
#     #     sleep(1.0)
#     #     dr.find_element_by_class_name('login_button').click()
#     #     sleep(1.0)
#
#     @data(['825069672, houec1019'])
#     def test_2(self, value):
#         # print(value)
#         a = value[0].split(',')
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d = login(self.dr, b, c)
#         print(d)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()



# from selenium import webdriver
# # from time import sleep
# # from ddt import ddt,file_data,data,unpack
# # import unittest
# # import xlrd
# # class wt(unittest.TestCase):
# #     def setUp(self):
# #         self.dr=webdriver.Firefox()
# #         self.dr.get('https://www.alltuu.com/')
# #         self.dr.implicitly_wait(10.0)
# #     def test_1(argument):
# #         argument.dr.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
# #         argument.dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[2]/div/input').send_keys('u')
# #         sleep(2)
# #         argument.dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[3]/div/input').send_keys('p')
# #         sleep(2)
# #         argument.dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[4]/div').click()
# #         argument.assertEqual(argument.dr.title,'喔图云')
# # if __name__=='__main__':
# #     unittest.main()

ab='abckdchan'
c=ab.split('c')
print(c)