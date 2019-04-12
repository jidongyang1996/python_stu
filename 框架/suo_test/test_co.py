#!/user/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
from 框架.config import 索赔
from 框架.data import 索赔读取
class suopei_case(unittest.TestCase):
    shuju=索赔读取.suopeiduqu()
    shuju123=shuju.duqu_jichushuju()
    def test_1(self):
        suo=索赔.suopei()
        asd=suo.jichushuju(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        suo = 索赔.suopei()
        asd = suo.jichushuju(int(self.shuju123[1][0]), int(self.shuju123[1][1]))
        self.assertEqual('get error',asd['message'])
if __name__=='__main__':
    unittest.main()
