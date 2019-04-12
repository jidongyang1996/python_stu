#!/user/bin/python
# -*- coding:utf-8 -*-
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Firefox()
# dr.get('https://www.taobao.com/')
# dr.find_element_by_xpath('//*[@id="q"]').send_keys('python')
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button').click()
# sleep(3)
#
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys('15237891832')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('jiyx960604')
# sleep(10)
# dr.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()



#自动登陆喔图云
from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get('https://www.alltuu.com')
dr.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[2]/ul/li[2]/div/a[1]').click()
dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[2]/div/input').send_keys('13526869794')
sleep(2)
dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[3]/div/input').send_keys('123456')
sleep(2)
dr.find_element_by_xpath('/html/body/div/div/div[2]/div/section[4]/div').click()
print(dr.title)


