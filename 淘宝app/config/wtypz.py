#!/user/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
def denglu(u,p):
    desired_caps = {'platformName': 'Android',
                    'deviceName': '127.0.0.1:62001',
                    'appPackage': 'com.alltuu.android',
                    'appActivity': 'android.alltuu.com.newalltuuapp.home.HomeActivity'}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(15)
    driver.find_element_by_class_name('android.widget.ImageView'[0]).send_keys('123443')
denglu(1,2)