from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time


class TwitterBot:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get("https://twitter.com/")
		time.sleep(3)
		email = bot.find_element_by_class_name("email-input")
		password = bot.find_element_by_name("session[password]")
		email.clear()
		password.clear()
		email.send_keys(self.email)
		password.send_keys(self.password)
		password.send_keys(keys.RETURN)
		time.sleep(3)

	def like_tweet(self, hashtag):
		bot = self.bot
		bot.get("https://twitter.com/search?q=" + hashtag + "&src=typd")
		time.sleep(2)

		#scroll down thrice to expose many tweets!
		for i in range(1,3):
			bot.execute_script(window.scrollTo(0,document.body.scrollHeight))
			time.sleep(2)
			tweets = bot.find_element_by_class_name("tweet")
			links = [elem.get_attribute("data-permalink-path") for elem in tweets] #Eg. /chris23/status/1248274212

			for link in links:
				bot.get("https://twitter.com" + link) #open tweet
				try:
					bot.find_element_by_class_name("HeartAnimation").click()  # like :)
					time.sleep(30) # important to avoid spam flagging
				except Exception as ex:
					time.sleep(30) # take a break before continuing


#main:wq
kirk = TwitterBot("kirkampong3@gmail.com", "xxxxxx")
kirk.login()
kirk.like_tweet("topic-of-interest")