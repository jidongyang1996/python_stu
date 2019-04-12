# # !/user/bin/python
# # -*- coding:utf-8 -*-
# from appium import webdriver
# import time
# desired_caps={'platformName':'Android',
#               # 'platformversion':'6.0',
#               'deviceName':'8BN0217912000957',
#               'appPackage':'com.netease.cloudmusic',
#               'appActivity':'.activity.LoadingActivity'}
# #
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# time.sleep(20)
# # driver.find_element_by_id('com.netease.cloudmusic:id/a5z').click()
# # time.sleep(3)
# # driver.find_element_by_id('com.netease.cloudmusic:id/aev').click()
# # time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15537831769')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('gao19930903')
# time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
# time.sleep(20)
# driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
# time.sleep(3)
# aa=driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
# if aa=='123':
#     print("fail")
# else:
#     print('pass')
# driver.quit()







from appium import webdriver
import unittest
from time import sleep
import xlrd
class wyy(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        # 'platformversion':'6.0',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': '.activity.LoadingActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(15)
        return self.driver
    def dq(self):
        shuju=[]
        f=xlrd.open_workbook(r'E:\python学习\手机自动化\wyyyl.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            a=sheet.row_values(i)
            if i == 0:
                continue
            else:
                shuju.append(a)
        # print(shuju)
        return shuju
    # def dq2(self):
    #     shuju2=self.dq()
    #     # for j in shuju2:
    #         # print(j)

    def dl(self,u,p):
        self.driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('u')
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('p')
        sleep(3)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        sleep(15)
        self.driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
        sleep(3)
        aa=self.driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
        return aa

    def test_1(self):
        a=self.dq()
        print(a)
        # b=self.dl(int(a[0][0]),a[0][1])
        # print(b)
        # self.assertEqual(b,123)






if __name__=='__main__':
    a=wyy()
    # a1=a.dakai()
    b=a.dq()

    unittest.main()
