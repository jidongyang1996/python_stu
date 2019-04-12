#!/user/bin/python
# -*- coding:utf-8 -*-
from ceshi.jianshu.config.tools import element
from selenium import  webdriver
from time import sleep


# a = element(r'E:\python学习\ceshi\jianshu\element\login.yaml')
# # 返回一个字典
# print(a)

#
# dr = webdriver.Chrome()
# dr.get("https://qzone.qq.com/")
# dr.implicitly_wait(5.0)
# dr.switch_to.frame(a['frame_id'])
# dr.find_element_by_id(a['login']['l_id']).click()
# dr.find_element_by_id(a['login']['u_id']).send_keys('825069672')
# sleep(1.0)
# dr.find_element_by_id(a['login']['p_id']).send_keys('houec1019')
# sleep(1.0)
# dr.find_element_by_id(a['login']['s_id']).click()
# dr.quit()


# 定义登录函数
def login(arg, username, password):
    arg.switch_to.frame('login_frame')
    arg.find_element_by_id('switcher_plogin').click()
    arg.find_element_by_id('u').send_keys(username)
    sleep(1.0)
    arg.find_element_by_id('p').send_keys(password)
    sleep(1.0)
    arg.find_element_by_id('login_button').click()
    return arg.title
