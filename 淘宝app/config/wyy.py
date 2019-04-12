#!/user/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
import time
def denglu(u,p):
    desired_caps={'platformName':'Android',
                  # 'platformversion':'6.0',
                  'deviceName':'8BN0217912000957',
                  'appPackage':'com.netease.cloudmusic',
                  'appActivity':'.activity.LoadingActivity'}
    #
    driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    time.sleep(20)
    driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    time.sleep(3)
    driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys(u)
    time.sleep(3)
    driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys(p)
    time.sleep(3)
    driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    time.sleep(20)
    driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
    time.sleep(3)
    aa=driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
    return aa