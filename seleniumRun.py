#!/usr/bin/env python3

from time import sleep

from selenium import webdriver

from instapy import InstaPy
from instapy import smart_run

class LoginPage():
	def __init__(self, browser):
		self.browser = browser
		self.credentials = []

	def loadCredentials(self):
		with open("credentials.txt") as f:
			for line in f.readlines():
				self.credentials.append(line)
		f.close()

	def login(self):
		self.browser.get('https://www.instagram.com/')
		self.browser.implicitly_wait(5)
		usernameIn = self.browser.find_element_by_xpath("//input[@name='username']")
		passwordIn = self.browser.find_element_by_xpath("//input[@name='password']")

		usernameIn.send_keys(self.credentials[0])
		passwordIn.send_keys(self.credentials[1])

		login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		login_button.click()
		sleep(5)

		return igFeedPage(self.browser, self.credentials)

	def close(self):
		self.browser.close()

class igFeedPage():
	def __init__(self, browser, credentials):
		self.browser = browser
		self.credentials = credentials
		self.comments = []
	
	def startInstaPySession(self):
		session = InstaPy(username= self.credentials[0],
                  password= self.credentials[1],
                  headless_browser=False)


def main():
	browser = webdriver.Firefox()
	ig = LoginPage(browser)
	ig.loadCredentials()
	ig.login()

	#ig.close()

if __name__ == "__main__":
	main()

