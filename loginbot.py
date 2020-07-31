from selenium import webdriver
from time import sleep
from passwords import *


class Instabot:
	def __init__(self,instausername,instapw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]").click()
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(instausername)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(instapw)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button").click()
		
	def inslogin(self):
		sleep(5)
		self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
		print("Select the Account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:Exit")
		choice = int(input("For Which account you need to login:"))

class FbBot:
	def __init__(self,fbusername,fbpw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.facebook.com")
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(fbusername)
		self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(fbpw)
	def fblogin(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()
		print("Select the Account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:Exit")
		choice = int(input("For Which account you need to login:"))
		
class TwitterBot:
	def __init__(self,twusername,twpw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://twitter.com/")
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[1]/div/label/div/div[2]/div/input").send_keys(twusername)
		self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[2]/div/label/div/div[2]/div/input").send_keys(twpw)
	def twlogin(self):	
		self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[3]/div/div/span/span").click()
		print("Select the Account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:Exit")
		choice = int(input("For Which account you need to login:"))
		
class GithubBot:
	def __init__(self,gitusername,gitpw):
		self.driver = webdriver.Chrome()
		self.driver.get("https://github.com/login")
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]").send_keys(gitusername)
		self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]").send_keys(gitpw)
	def gitlogin(self):
		self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]").click()
		print("Select the Account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:Exit")
		choice = int(input("For Which account you need to login:"))
		


print("**************************Welcome To The AppBot!*************************")
print("Select the Account:\n0:Instagram\n1:Facebook\n2:Twitter\n3:Github\n4:Exit")
choice = int(input("For Which account you need to login:"))
if choice==0:
	mybot = Instabot(instausername,instapw)
	mybot.inslogin()
elif choice==1:
	mybot = FbBot(fbusername,fbpw)
	mybot.fblogin()
	
elif choice==2:
	mybot = TwitterBot(twusername,twpw)
	mybot.twlogin()

elif choice==3:
	mybot = GithubBot(gitusername,gitpw)
	mybot.gitlogin()
else:
	pass