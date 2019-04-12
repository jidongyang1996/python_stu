# #!/user/bin/python
# # -*- coding:utf-8 -*-
# 接口，请求传参和结果对比
# http协议  用requests
# import requests
# # import json
# import unittest
# # unittest      #单元测试框架
# # #主要是对用例进行管理，执行
# #面向对象
# #所有的用例函数必须以test开头
# class suopei(unittest.TestCase):
#     def test_1(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             'Content-Type': 'application/json',
#             'x-dealer-code': '2100150',
#             'x-position-code': 'D_PO_1028',
#             'x-resource-code': 'BASIC_DATA',
#             'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#             'x-user-code': 'djy0mx',
#             'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
#             }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes=res.json()
#         self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')
#     def test_2(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             'Content-Type': 'application/json',
#             'x-dealer-code': '2100150',
#             'x-position-code': 'D_PO_1028',
#             'x-resource-code': 'BASIC_DATA',
#             'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#             'x-user-code': 'djy0mx',
#             'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes = res.json()
#         self.assertNotEqual(mes['data']['applicationType'][0]['name'],'多装')
#     def test_3(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             'Content-Type': 'application/json',
#             'x-dealer-code': '2100150',
#             'x-position-code': 'D_PO_1028',
#             'x-resource-code': 'BASIC_DATA',
#             'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#             'x-user-code': 'djy0mx',
#             'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes = res.json()
#         self.assertEqual(mes['data']['applicationType'][0]['value'], '1')
#     def test_4(self):
#         url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
#         head = {
#             'Content-Type': 'application/json',
#             'x-dealer-code': '2100150',
#             'x-position-code': 'D_PO_1028',
#             'x-resource-code': 'BASIC_DATA',
#             'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#             'x-user-code': 'djy0mx',
#             'x-access-token': 'da05ee37e5676e7b27972b2892e0fdeb',
#         }
#         body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#             'utf-8')
#         res = requests.post(url, headers=head, data=body)
#         mes = res.json()
#         self.assertNotEqual(mes['data']['applicationType'][0]['value'], '多装')
#
#
# if __name__=='__main__':
#     unittest.main()
# # main 检测类中所有以test开头的函数
# #先执行谁，是比较test后面的字符，谁在前执行谁
#
#
#
#
# import requests
# import unittest
# class wo(unittest.TestCase):
#     def setUp(self):
#     #是每次执行用例之前，每个用例都执行一次
#     #初始化测试环境，让测试环境变成最开始的状态
# #setupClass  在所有用例之前，只执行一次
#         print('hello')
#     def test_1(self):
#         print(123)
#         self.assertEqual(123,123)
#     def test_2(self):
#         print(432)
#         self.assertEqual(432,432)
#     def tearDown(self):
#     #是每次用例结束之后执行
#     #清理测试环境
#         print('world')
#
# #任何测试用例都要在相同的环境下执行
# if __name__=='__main__':
#     unittest.main()
#
# #
# #
# # url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
# # head={
# #     'Content-Type':'application/json',
# #     'x-dealer-code':'2100150',
# #     'x-position-code':'D_PO_1028',
# #     'x-resource-code':'BASIC_DATA',
# #     'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
# #     'x-user-code':'djy0mx',
# #     'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb',
# }
# body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
# res=requests.post(url,headers=head,data=body)
# # print(res.text)
# mes=json.loads(res.text)
# #或者可写mes=res.json()
# print(mes['data']['applicationType'][0]['name'])
# #断言
# assert mes['data']['applicationType'][0]['name'] == '多装'
# assert mes['data']['applicationType'][0]['value'] == '1'
#
# unittest      #单元测试框架
# #主要是对用例进行管理，执行