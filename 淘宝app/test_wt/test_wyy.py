#!/user/bin/python
# -*- coding:utf-8 -*-
from 淘宝app.data import wyysj
from 淘宝app.config import wyy
import unittest
class wyycs(unittest.TestCase):
    a=wyysj.duqu()
    def test_1(self):
        b=wyy.denglu(int(self.a[0][0]),self.a[0][1])
        self.assertEqual(b,'亚的网易云没有名')
if __name__=='__main__':
    unittest.main()