#!/user/bin/python
# -*- coding:utf-8 -*-
from 框架.report import HTMLTestRunnertest
from 淘宝app.test_wt.test_wyy import wyycs
import unittest
def wyybg():
    suit=unittest.TestSuite()
    suit.addTest(unittest.makeSuite(wyycs))
    f = open(r'E:\python学习\淘宝app\report\wyy.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(stream=f, title='索赔测试报告', tester='纪栋洋', description='结果如下')
    runner.run(suit)
    f.close()


if __name__ == '__main__':
    wyybg()