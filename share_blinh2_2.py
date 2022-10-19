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
from selenium.webdriver.common.by import By
# import undetected_chromedriver as webdriver



# lấy số tài khoản và mật khẩu clone
table = pd.read_excel("clone2.xlsx")

list_tk_clone = list(table["email"])
list_mk_clone = list(table["password"])
stt = 0 
while True:
	print("dangnhap")
	driver = webdriver.Chrome()
	# chrome_options = webdriver.ChromeOptions()
	# pref2 = {"profile.default_content_setting_values.notifications": 2}
	# chrome_options.add_experimental_option("prefs", pref2)
	options = webdriver.ChromeOptions()
	options.add_argument('--disable-notifications')
	driver = webdriver.Chrome(options=options)
	
	driver.get('https://www.facebook.com/')
	driver.maximize_window()
	# table = driver.find_element_by_class_name('_9vtf')
	table = driver.find_element(By.CLASS_NAME, '_9vtf')
	# rows = table.find_elements_by_tag_name('div')
	rows = table.find_elements(By.TAG_NAME,'div')
	
	account = randint(0, len(list_tk_clone)-1)
	# account = 3
	
	for a in rows:
		# tendangnhap = a.find_element_by_id('email')
		tendangnhap = a.find_element(By.ID, "email")
		tendangnhap.send_keys(list_tk_clone[account])
		sleep(randint(1, 3))
		# matkhau = a.find_element_by_id('pass')
		matkhau = a.find_element(By.ID, "pass")
		matkhau.send_keys(list_mk_clone[account])
		sleep(randint(1, 3))
		break
	# dangnhap = table.find_element_by_class_name('_6ltg').click()
	dangnhap = table.find_element(By.CLASS_NAME,"_6ltg").click()
	sleep(randint(3, 5))
	
	driver.get('https://www.facebook.com/Ngoisaoxanhmoncity/photos/a.1611875852208734/5834648766598067/')
	sleep(randint(3, 5))
	for action in range(0,15):
		# try:
		# buttons = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']")
		buttons = driver.find_elements(By.XPATH,"//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa']")
		for button in buttons:
			if 'Share' in button.text:
				button.click()
				break
		sleep(randint(3, 5))
		# share_now = driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m']")
		share_now = driver.find_element(By.XPATH,"//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h']")
		share_now.click()
		stt+=1 
		print('Da share lan thu '+ str(stt))
		sleep(randint(3, 5))
		# except:
			# pass
	driver.quit()

