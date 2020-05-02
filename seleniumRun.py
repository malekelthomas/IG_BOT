#!/usr/bin/env python3

from time import sleep

from selenium import webdriver


browser = webdriver.Firefox()


browser.get('https://www.instagram.com/')

usernameInput = browser.find_element_by_name("username") #finds HTML element with username tag, in this case the username text field

usernameInput.send_keys("lekedraws") #enters text into field 

passwordInput = browser.find_element_by_name("password")

passwordInput.send_keys("pw")

browser.sleep(5)

browser.close()