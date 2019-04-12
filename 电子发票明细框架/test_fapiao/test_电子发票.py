#!/user/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
from 电子发票明细框架.config import 电子发票URL
from 电子发票明细框架.data import 电子发票读取
class fapiaoceshi(unittest.TestCase):
    shuju=电子发票读取.fapiaoduqu()
    shuju123=shuju.dqjcsj()
    def test_1(self):
        ce=电子发票URL.fapiao()
        asd=ce.jcsj(int(self.shuju123[0][0]),int(self.shuju123[0][1]),int(self.shuju123[0][2]))
        self.assertEqual(asd['totalSize'],0)

    def test_2(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[1][0]),(self.shuju123[1][1]),(self.shuju123[1][2]))
        self.assertEqual(asd['message'],'get error')

    def test_3(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[2][0]),(self.shuju123[2][1]),(self.shuju123[2][2]))
        self.assertEqual(asd['message'],'get error')

    def test_4(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[3][0]),(self.shuju123[3][1]),(self.shuju123[3][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_5(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[4][0]),(self.shuju123[4][1]),(self.shuju123[4][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_6(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[5][0]),(self.shuju123[5][1]),(self.shuju123[5][2]))
        self.assertEqual(asd['totalSize'],0)

    def test_7(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[6][0]),(self.shuju123[6][1]),(self.shuju123[6][2]))
        self.assertEqual(asd['totalSize'],0)

    def test_8(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[7][0]),(self.shuju123[7][1]),(self.shuju123[7][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_9(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[8][0]),(self.shuju123[8][1]),(self.shuju123[8][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_10(self):
        ce = 电子发票URL.fapiao()
        asd = ce.jcsj((self.shuju123[9][0]),(self.shuju123[9][1]),(self.shuju123[9][2]))
        self.assertEqual(asd['message'], 'get error')


if __name__=='__main__':
    unittest.main()
