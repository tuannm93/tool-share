# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:13:53 2022

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:15:09 2022

@author: Admin
"""

from time import sleep
from selenium import webdriver
from random import randint
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

table = pd.read_excel("clone.xlsx")

list_tk_clone = list(table["email"])
list_mk_clone = list(table["password"])

stt = 0

while True:
    print("dangnhap")
    chrome_options = webdriver.ChromeOptions()
    pref2 = {"profile.default_content_setting_values.notifications": 2}
    # mobile_emulation = {
    # "deviceMetrics": { "width": 400, "height": 626, "pixelRatio": 3.0 },
    # "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19" }
    mobile_emulation = { "deviceName": "Nexus 5" }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("prefs", pref2)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com/')
    # driver.maximize_window()
    
    # dang nhap 
    account = randint(0, len(list_tk_clone)-1)
    # tendangnhap = driver.find_element_by_xpath("//input[@type='email']")
    tendangnhap = driver.find_element(By.XPATH,"//input[@type='email']")
    tendangnhap.send_keys(list_tk_clone[account])
    sleep(randint(1, 3))
    # matkhau = driver.find_element_by_xpath("//input[@type='password']")
    matkhau = driver.find_element(By.XPATH,"//input[@type='password']")
    matkhau.send_keys(list_mk_clone[account])
    sleep(randint(1, 3))
        
    # dangnhap = driver.find_element_by_xpath("//button[@name='login']").click()
    dangnhap = driver.find_element(By.XPATH,"//button[@name='login']").click()
    sleep(randint(3, 5))
    
    try:
        # submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
        sleep(randint(1, 3))
    except:
        pass
    
    for actions in range(0, 20):
        action = randint(1, 3)
        # action = 3
        # giả vờ lướt newfeed để facebook không chặn
        if action == 1:
            driver.get('https://m.facebook.com/')
            print('luot newfeed')
            sleep(randint(1, 3))
            # luot_new_feed
            scroll = randint(0, 5)
            for i in range(scroll, 10):
                sleep(randint(1, 5))
                scroll += 1
                scroll1 = randint(100, 600)
                driver.execute_script(
                    "window.scrollBy(0,{})".format(scroll1), "")
                
        if action == 2:
            print("xem story")
            #click_story
            driver.get('https://m.facebook.com/')
            sleep(randint(3, 5))
            # button_list = driver.find_elements_by_xpath("//div[@role='button']")
            button_list = driver.find_elements(By.XPATH,"//div[@role='button']")
            for button in button_list:
                if button.get_attribute("aria-label") is None:
                    continue
                
                if "story" in button.get_attribute("aria-label"):
                    button.click()
                    sleep(randint(3, 7))
                    break
        if action == 3:
            print('Share')
            try:
                driver.get("https://m.facebook.com/sharer.php?fs=7&sid=pfbid02noMHyoRgoEd41A52zkGtMC6bmEVUv8ZRuA8zKwjZdErACMsaaSxnYqdh2fffmQmol&eav=AfZvQsmPThPlXf_GUDxO_pINZ32lZrvjgqCUra0kJgCOjk3zvEyPt_UC8CqESWg8IZM&paipv=0")
                sleep(randint(3, 5))
                # post = driver.find_element_by_xpath("//button[@value='Post']")
                post = driver.find_element(By.XPATH,"//button[@value='Post']")
                post.click()
                sleep(randint(3, 5))
                try:
                    # block = driver.find_element_by_xpath("//a[@class='_6j_c']").text
                    block = driver.find_element(By.XPATH,"//a[@class='_6j_c']").text
                    print(block)
                    if "You can't use this feature at the moment" in block:
                        # list_tk_clone.pop(account)
                        # list_mk_clone.pop(account)
                        driver.quit()
                        break
                except:
                    pass
                # text = driver.find_element_by_xpath("//div[@class='m fixed-container top']").text
                text = driver.find_element(By.XPATH,"//div[@class='m fixed-container top']").text
                if "Your post" in text:
                    stt+=1 
                    print('Da share lan thu '+ str(stt))
            except:
                continue
    driver.quit()
