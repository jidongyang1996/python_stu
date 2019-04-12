#!/user/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
def qq(u,p):
    dr=webdriver.Firefox()
    dr.get('https://www.alltuu.com/')
    dr.implicitly_wait(10.0)
    dr.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
    dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[2]/div/input').send_keys(u)
    sleep(2)
    dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[3]/div/input').send_keys(p)
    sleep(2)
    dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[4]/div').click()
    sleep(3)
    a=dr.find_element_by_class_name('nav-header-right-userNick').text
    return a