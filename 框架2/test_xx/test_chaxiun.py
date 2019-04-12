#!/user/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
from 框架2.config import souye
from 框架2.delete.duqu import diqushuju
class daoru(unittest.TestCase):
    shuju=diqushuju.duqu_jichushuju()
    def test_1(self):
        cha=souye.xuexiao()
        asd=cha.jichushuju(self.shuju[0][0])
        self.assertEqual(asd['code'],0)
if __name__=='__main__':
    unittest.main()
