#!/user/bin/python
# -*- coding:utf-8 -*-
import HTMLTestRunnertest
from 框架.report import HTMLTestRunnertest
from 框架.suo_test.test_suopei import suopei_case
import unittest
def baogao_(aa):
    suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(suopei_case))  #写类名,适合本文件的
    for o in aa:
        dis=unittest.defaultTestLoader.discover(r'E:\python学习\框架\suo_test',pattern='test_{}.py'.format(o.strip()))  #需要两个参数  1.路径  2.匹配条件
                                                                         #可写“test*.py',也可传参aa意思是到这个路径下，匹配所有的以test开头的文件，然后test文件中找到函数以test开头
        for i in dis:
            suit.addTest(i)
    f=open(r'E:\python学习\框架\report\c.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='索赔测试报告',tester='纪栋洋',description='结果如下')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    baogao_()