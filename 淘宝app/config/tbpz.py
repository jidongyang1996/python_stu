#!/user/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
def denglu(u,p):
    desired_caps = {'platformName': 'Android',
                    'deviceName': '127.0.0.1:62001',
                    'appPackage': 'com.taobao.taobao',
                    'appActivity': 'com.taobao.tao.TBMainActivity'}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(15)
    driver.find_element_by_class_name('android.widget.FrameLayout').click()
    time.sleep(3)
    driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_switch_pwdlogin').click()
    time.sleep(3)
    driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_account_et').send_keys(u)
    time.sleep(3)
    driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_password_et').send_keys(p)
    time.sleep(3)
    driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_login_btn').click()
    time.sleep(3)

    return driver


