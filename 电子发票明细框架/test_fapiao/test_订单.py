#!/user/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
from 电子发票明细框架.config import 查询订单列表URL
from 电子发票明细框架.data import 订单列表读取
class dingdanceshi(unittest.TestCase):
    shuju=订单列表读取.dingdanduqu()
    shuju123=shuju.dqddlb()
    def test_1(self):
        ce=查询订单列表URL.cxddlb()
        asd=ce.ddlb(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['totalSize'],9)

    def test_2(self):
        ce=查询订单列表URL.cxddlb()
        asd=ce.ddlb(int(self.shuju123[1][0]),int(self.shuju123[1][1]))
        self.assertEqual(asd['message'],'get error')

    def test_3(self):
        ce=查询订单列表URL.cxddlb()
        asd=ce.ddlb(int(self.shuju123[2][0]),int(self.shuju123[2][1]))
        self.assertEqual(asd['message'],'get error')

if __name__=='__main__':
    unittest.main()
