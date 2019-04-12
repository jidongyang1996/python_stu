#!/user/bin/python
# -*- coding:utf-8 -*-
import HTMLTestRunnertest
from 电子发票明细框架.report import HTMLTestRunnertest
import unittest
def fapiaobaogao(o):
    suit=unittest.TestSuite()
    for i in o:
        dis = unittest.defaultTestLoader.discover(r'E:\python学习\电子发票明细框架\test_fapiao',pattern='test_{}.py'.format(i))
        for j in dis:
            suit.addTest(j)
    f = open(r'E:\python学习\电子发票明细框架\report\电子发票报告x.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(stream=f, title='索赔测试报告', tester='纪栋洋', description='结果如下')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    fapiaobaogao(o)

