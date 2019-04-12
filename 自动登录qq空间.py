#!/user/bin/python
# -*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# print(dr.title)
# #切换到某一个框架
# dr.switch_to.frame('login_frame')     #处理框架  也叫iframe(窗口)，括号内可写框架的id或name或者先定位到框架
# 回到最开始框架中
# dr.switch_to.default_content()
# #回到父框架页面中
# dr.switch_to.parent_frame()
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('844117069')
# sleep(2)
# dr.find_element_by_id('p').send_keys('jiyx123456')
# sleep(2)
# dr.find_element_by_id('login_button').click()
#
# 获取当前窗口的字符串（句柄）
# dr.get('https://www.douban.com/')
# print(dr.current_window_handle)
# dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
# sleep(2)
# #获取所有窗口的句柄
# qq=dr.window_handles
# print(qq)
# # #切换句柄(参数只能是句柄)
# dr.switch_to.window(qq[-1])
# sleep(2)
# print(dr.title)
#
#
#
#
# 自动登陆qq邮箱
# from selenium import webdriver
# from time import sleep
# we=webdriver.Firefox()
# we.get('https://mail.qq.com/cgi-bin/loginpage')
# we.switch_to.frame('login_frame')
# we.find_element_by_class_name('switch_btn').click()
# sleep(2)
# we.find_element_by_class_name('inputstyle').send_keys('844117069')
# sleep(2)
# we.find_element_by_id('p').send_keys('jiyx123456')
# sleep(2)
# we.find_element_by_class_name('btn').click()
#
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('https://y.qq.com/')
# ac=dr.find_element_by_class_name('query-search__border__item').find_elements_by_tag_name('a')
# print(len(ac))