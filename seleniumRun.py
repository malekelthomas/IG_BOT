#!/usr/bin/env python3

from time import sleep

from selenium import webdriver

from instapy import InstaPy
from instapy import smart_run

class LoginPage():
	""" Represents the instagram login page as an object for use with instapy."""
	
	def __init__(self, browser):
		""" Initializes the object with the supplied browser, and a list that will contain its credentials"""
		
		self.browser = browser
		self.credentials = []

	def loadCredentials(self):
		""" Opens file containing username and password and stores them into the credentials list"""
		with open("credentials.txt") as f:
			for line in f.readlines():
				self.credentials.append(line.strip())
		f.close()

	def login(self):
		""" Uses webdriver to navigate to the login page of instagram. Then it enters in credentials, locates the login button and clicks it. Returns the next page which is the instagram feed.""" 
		
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
		""" Closes browser """
		self.browser.close()

class igFeedPage():
	def __init__(self, browser, credentials):
		""" Initializes object with the supplied browser, credentials for instaPy, and a list of comments that will be used by the instaPy module""" 
		
		self.browser = browser
		self.credentials = credentials
		self.comments = []
	
	def startInstaPySession(self):
		""" Starts an InstaPy session"""
		
		session = InstaPy(username= self.credentials[0],
                  password= self.credentials[1],
                  headless_browser=False)

		with smart_run(session):
			accs = ["maleke_t"]
			session.follow_by_list(accs, times=1, sleep_delay=600, interact=False)

	def getCredentials(self):
		return self.credentials

def main():
	browser = webdriver.Firefox()
	loginPage = LoginPage(browser)
	loginPage.loadCredentials()
	feedPage = loginPage.login()

	#print(feedPage.getCredentials())
	feedPage.startInstaPySession()


	#ig.close()

if __name__ == "__main__":
	main()

