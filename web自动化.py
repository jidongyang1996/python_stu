#!/user/bin/python
# -*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
#
# 定义使用什么浏览器
# dr = webdriver.Firefox()
# 打开网址
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(2)
# # #获取网址的标题
# # print(dr.title)
# # #获取打开网页的网址
# # print(dr.current_url)
# dr.get('https://www.jd.com')
# sleep(2)
# #回退
# dr.back()
# sleep(2)
# #前进
# dr.forward()
# sleep(2)
#
# # #设置浏览器大小
# dr.set_window_size(400,400)
# #
# # #设置浏览器位置
# dr.set_window_position(600,500)
#
# # #设置浏览器全屏(最大化），最小化
# dr.maximize_window()
# dr.minimize_window()
# sleep(2)
# #关闭浏览器，close是关闭浏览器，不断开连接     quit是关闭浏览器，断开连接
# dr.quit()
# # dr.close()
#
#
# 定位   是核心
# 1.通过id定位  标签的id属性
# dr.find_element_by_id('kw').send_keys('linux')   #搜索框中输入linux
# sleep(2)
# dr.find_element_by_id('su').click()  #点击百度一下
#
# 2.通过class_name定位   标签的class属性
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# dr.find_element_by_class_name('bg s_btn ').click()
#
# 3.通过name定位    标签上的name属性
# dr.find_element_by_name('tj_trmap').click()  #点击百度地图
#
# 4.text定位   标签的文本定位
# dr.find_element_by_link_text('hao123').click()  #点击好123
#
# 5.partial_link_text定位    标签的模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()   #模糊定位，点击好123
#
# 6.tag_name 定位   标签名称定位
# 最不唯一的一个定位，通常用来定位一组元素
# dr.find_element_by_tag_name('input')
#
# 7.css_selector定位   css定位
# dr.find_element_by_css_selector('#kw').send_keys('11')
#
# 8.xpath定位   路径定位
# xpath 路径标记语言
# xml 可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]')   #/是绝对路径      //是相对路径
#
# 查询级别  id >  css >  xpath  >name >class_name……
#
# 定位一组数据(element加s）  对多个数据进行操作时
# wd=dr.find_elements_by_class_name('mnav')
# for i in wd:
#     if i.text=='hao123':
#         continue
#     else:
#         dr.get(i.get_attribute('href'))
#         sleep(2)
#         dr.back()
#
# 层级定位   遇到复杂的元素的定位   父元素只能是单个元素   子元素可以是多个
# aa=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# print(len(aa))
# # for i in aa:
#     i.click()
#     sleep(2)
#
#
# 模拟动作（定位到的数据只能做一次动作）
# send_keys()  输入
# click        点击
# text         获取定位到的元素的文本
# clear()      清空定位到的元素上面的数据
#
#
# 模拟鼠标的动作
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.jd.com')
# sleep(2)
# wr=dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul').find_element_by_tag_name('li')
# sleep(2)
# for i in wr:
#     #控制鼠标来移动到元素的位置上          执行
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os
# import selenium.webdriver.support.ui as ui
# from time import sleep
# dr=webdriver.Chrome()
# # #处理弹出框
# dr.get('http://www.jd.com')
# #切换到弹出框
# ww=dr.switch_to_alert()
# while True:
#     # 获取弹出框上面的内容
#     print(ww.text)
#     #点击确定
#     ww.accept()
#     sleep(2)
#     #点击取消
#     ww.dismiss()
#     #输入
#     ww.send_keys('内容')
#     sleep(2)
#
#
#
# #处理页面滚动条  javascript代码
# for i in range(1,10000,2000):
#
#     js="var q=document.documentElement.scrollTop={}".format(i)
# #执行javascript语句
#     dr.execute_script(js)
#     sleep(2)
#
#
# 显性等待
# implicitly_wait(10.0)
# 强制等待
# sleep(2)
# 智能等待  设置一个最大等待时间，检测到某个元素出现，就不会继续等待
# 设置最大等待时间
# unit =ui.WebDriverWait(dr,10)
# #直到定位的元素出现，就不会等待了
# unit.until(lambda dr:dr.find_element_by_class_name('label').is_displayed())
# print('hello')
#
#
# #
# w=dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[2]/a[1]')
# #获取定位到的元素某个属性的值
# a=w.get_attribute('class')
# print(a)

import unittest
from ddt import ddt,data,unpack

@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')
    @data([1,2,3])
    def test_1(self,value):
        print(value)


unittest.main()
