#!/user/bin/python
# -*- coding:utf-8 -*-
from qq空间测试.config import 喔图云URL
from qq空间测试.data import 账号密码读取
import unittest
class wty(unittest.TestCase):

    a=账号密码读取.zhmaduqu()
    b=a.dqsj()
    def test_1(self):
        c=喔图云URL.qq(int(self.b[0][0]),self.b[0][1])
        self.assertEqual(c,'登录 | 注册')
    def test_2(self):
        c=喔图云URL.qq(int(self.b[1][0]),self.b[1][1])
        self.assertEqual(c,'登录 | 注册')
    def test_3(self):
        c=喔图云URL.qq(int(self.b[2][0]),self.b[2][1])
        self.assertEqual(c,'登录 | 注册')
if __name__=='__main__':
    unittest.main()