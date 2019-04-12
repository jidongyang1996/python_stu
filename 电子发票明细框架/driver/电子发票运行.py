#!/user/bin/python
# -*- coding:utf-8 -*-
from 电子发票明细框架.report.电子发票报告 import fapiaobaogao
def run(o):
    fapiaobaogao(o)
with open('回归.txt','r')as f:
    a= f.readlines()
    if len(a)==1:
        run('*')
    else:
        run(a)
