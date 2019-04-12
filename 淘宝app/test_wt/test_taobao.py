#!/user/bin/python
# -*- coding:utf-8 -*-
from 淘宝app.config import tbpz
from 淘宝app.data import shuju
import unittest
import time
class dlcs(unittest.TestCase):
    a=shuju.duqu()
    def test_1(self):
        b=tbpz.denglu(int(self.a[0][0]),self.a[0][1])
        time.sleep(3)
        # b.find_element_by_class_name()
        self.assertEqual(b,'我')

if __name__=='__main__':
    unittest.main()

