#!/usr/bin/env python3

from time import sleep

from selenium import webdriver

class LoginPage():
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.logininfo = []

	def loadCredentials(self):
		with open("credentials.txt") as f:
			for line in f.readlines():
				self.logininfo.append(line)
		f.close()

	def login(self):
		self.browser.get('https://www.instagram.com/')
		self.browser.implicitly_wait(5)
		usernameIn = self.browser.find_element_by_xpath("//input[@name='username']")
		passwordIn = self.browser.find_element_by_xpath("//input[@name='password']")

		usernameIn.send_keys(self.logininfo[0])
		passwordIn.send_keys(self.logininfo[1])

		login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()

	def close(self):
		self.browser.close()


def main():
	ig = LoginPage()
	ig.loadCredentials()
	ig.login()
	sleep(5)
	ig.close()

if __name__ == "__main__":
	main()

