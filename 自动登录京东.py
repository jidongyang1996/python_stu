#!/user/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Firefox()
dr.get('https://www.jd.com')
sleep(3)
dr.find_element_by_class_name('link-login').click()
sleep(3)
dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]').click()
sleep(3)
dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('15237891832')
sleep(3)
dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('jiyx123456')
sleep(3)
dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
sleep(2)
start=dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
#拖拽    drag_and_drop (起始位置，结束位置）
#拖拽    drag_and_drop_by_offset (起始位置，x轴坐标，y轴坐标）
ActionChains(dr).drag_and_drop_by_offset(start,156,0,).perform()
sleep(2)
dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
sleep(3)
dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
sleep(5)
# print(dr.current_window_handle)
dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
sleep(5)
# abc=dr.window_handles
# print(abc)
dr.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]').click()
sleep(3)
# dr.switch_to.window(abc[1])
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
