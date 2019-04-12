#!/user/bin/python
# -*- coding:utf-8 -*-
import HTMLTestRunnertest
import unittest
def wtbaogao(o):
    suit=unittest.TestSuite()
    for i in o:
        dis = unittest.defaultTestLoader.discover(r'E:\python学习\qq空间测试\test_空间',pattern='test_{}.py'.format(i))
        for j in dis:
            suit.addTest(j)
    f = open(r'E:\python学习\qq空间测试\report\wty.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(stream=f, title='索赔测试报告', tester='纪栋洋', description='结果如下')
    runner.run(suit)
    f.close()

