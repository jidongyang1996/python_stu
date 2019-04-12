#!/user/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
dr=webdriver.Firefox()
dr.get('https://www.iqiyi.com/')
dr.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div[4]/div[6]/div[1]/div/a/img').click()
sleep(3)
dr.switch_to.frame('login_frame')
dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div[2]/p/span/a[1]').click()
sleep(3)
dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/p').send_keys('13526869794')
sleep(3)
dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/p').send_keys('jiyx960604')
sleep(10)
dr.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div[3]/div[1]/span[1]/input').send_keys('海贼王')
sleep(3)
abc=dr.window_handles
print(abc)