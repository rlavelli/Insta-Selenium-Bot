from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Functions
def find_element_click(type_path, path, wd, await_after):
	element = wd.find_element(type_path, path)
	element.click()
	sleep(await_after)
def find_element_send_keys(type_path, path, keys, wd, await_after):
	element = wd.find_element(type_path, path)
	element.send_keys(keys)
	sleep(await_after)
	
#https://chromedriver.chromium.org/downloads
chromedriver_path = r'path-to-chrome-driver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/p/link-to-a-post/')
sleep(4)

#webdriver.find_element(By.XPATH,'')
cookie_path = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'
access_path = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/div[1]/a/button/div'
username_path = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input'
password_path = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input'
login_btn = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'
not_now_btn = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button'
comment_area = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea'
send_btn = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div[2]/div'

# Cookie agree
find_element_click(type_path=By.XPATH, path=cookie_path, wd=webdriver, await_after=4)

# Access
find_element_click(type_path=By.XPATH, path=access_path, wd=webdriver, await_after=4)

# Credentials
find_element_send_keys(type_path=By.XPATH, path=username_path, keys='my-user-name', wd=webdriver, await_after=2)
find_element_send_keys(type_path=By.XPATH, path=password_path, keys='my-password', wd=webdriver, await_after=2)

# Login
find_element_click(type_path=By.XPATH, path=login_btn, wd=webdriver, await_after=10)

# Not Now
find_element_click(type_path=By.XPATH, path=not_now_btn, wd=webdriver, await_after=6)


comments = ["commento1", "commento2", "commento3"] 
for c in comments:
	# Comment Area
	find_element_click(type_path=By.XPATH, path=comment_area, wd=webdriver, await_after=2)
	find_element_send_keys(type_path=By.XPATH, path=comment_area, keys=c, wd=webdriver, await_after=2)
	# Send
	find_element_click(type_path=By.XPATH, path=send_btn, wd=webdriver, await_after=5)


