# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 16:39:00 2022

@author: Admin
"""

from time import sleep
from selenium import webdriver
from random import randint
from selenium.common.exceptions import NoSuchElementException
import pandas as pd



# lấy số tài khoản và mật khẩu clone
table = pd.read_excel("clone.xlsx")

list_tk_clone = list(table["email"])
list_mk_clone = list(table["password"])
stt = 0 
while True:
    print("dangnhap")
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    pref2 = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", pref2)
    driver.get('https://www.facebook.com/')
    driver.maximize_window()
    table = driver.find_element_by_class_name('_9vtf')
    rows = table.find_elements_by_tag_name('div')
    
    account = randint(0, len(list_tk_clone)-1)
    # account = 3
    
    for a in rows:
        tendangnhap = a.find_element_by_id('email')
        tendangnhap.send_keys(list_tk_clone[account])
        sleep(randint(1, 3))
        matkhau = a.find_element_by_id('pass')
        matkhau.send_keys(list_mk_clone[account])
        sleep(randint(1, 3))
        break
    dangnhap = table.find_element_by_class_name('_6ltg').click()
    sleep(randint(3, 5))
    
    driver.get('https://www.facebook.com/photo/?fbid=3303540236593689&set=a.1402585900022475')
    sleep(randint(3, 5))
    for action in range(0,50):
        try:
            buttons = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']")
            for button in buttons:
                if 'Share' in button.text:
                    button.click()
                    break
            sleep(randint(3, 5))
            share_now = driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m']")
            share_now.click()
            stt+=1 
            print('Da share lan thu '+ str(stt))
            sleep(randint(3, 7))
        except:
            pass
    driver.quit()

