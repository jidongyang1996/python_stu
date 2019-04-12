#!/user/bin/python
# -*- coding:utf-8 -*-
# import requests
# import unittest
# class lx(unittest.TestCase):
#     def test_1(self):
#         url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head={
#             'Content-Type': 'application/json',
#             'x-dealer-code': '2100150',
#             'x-position-code': 'D_PO_1028',
#             'x-resource-code': 'BASIC_DATA',
#             'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#             'x-user-code': 'djy0mx',
#             'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'
#         body=body.encode('utf-8')
#         res=requests.post(url=url,headers=head,data=body)
#         mes=res.json()
#         print(mes)
# if __name__=='__main__':
#     unittest.main()


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
#     @data(['2385217201,jiyx123456'])
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

# import  unittest
# from selenium import webdriver
# from time import sleep
#
#
# class zhengjiang(unittest.TestCase):
#
#     def  setUp(self):
#         self.dr=webdriver.Firefox()
#         self.dr.get('https://ai.taobao.com/')
#     def test_01(self):
#         self.dr.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/div/a[1]').click()
#         sleep(2)
#         self.dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()
#         sleep(2)
#         self.dr.find_element_by_id('TPL_username_1').send_keys('qq1258153711')
#         sleep(2)
#         self.dr.find_element_by_id('TPL_password_1').send_keys('special1314...')
#         sleep(2)
#         self.dr.find_element_by_id('J_SubmitStatic').click()
#         sleep(3)
#         self.assertEqual(self.dr.title,'爱淘宝-淘宝网购物分享平台')
#
#     def tearDown(self):
#
#         self.dr.quit()
# if __name__=='__main__':
#     unittest.main()



def ac(a,b):
    print(a)
    print(b)
ac(1,2)