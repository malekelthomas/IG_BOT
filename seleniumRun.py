#!/usr/bin/env python3

from time import sleep

from selenium import webdriver


browser = webdriver.Firefox()

logininfo = []

with open("credentials.txt") as f:
	for line in f.readlines():
		logininfo.append(line)
	f.close()


browser.get('https://www.instagram.com/')

usernameInput = browser.find_element_by_name("username") #finds HTML element by name field, in this case the username text field

usernameInput.send_keys(logininfo[0]) #enters text into field 


passwordInput = browser.find_element_by_name("password")

passwordInput.send_keys(logininfo[1])

login_button = browser.find_element_by_xpath("//button[@type='submit']")

login_button.click()

sleep(5)

browser.close()