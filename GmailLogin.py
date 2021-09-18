''' 

Automate your gmail login using python
Command- python3 <file-name>

Requirements - 
pip install selenium - to automate the browser content
webdriver module for calling chrome

pip install chromedriver_binary - to have the latest chrome or the driver module
chromedrivermanager helps to get the latest chrome version

getpass module - helps the user to enter the password without being displayed to the screen
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

#To get the username or email id of the user
gmailid=input("Enter your email id:")

pwd = getpass("Enter the password:")

#To open google chrome webpage
driver = webdriver.Chrome(ChromeDriverManager().install())

#To delete all cookies
driver.delete_all_cookies()

#To open gmail login page
driver.get("https://www.gmail.com")

#Navigating and find the username box, to enter your username
driver.find_element_by_id("identifierId").send_keys(gmailid)

time.sleep(2)

#NAvigating to go to next button on the page
# driver.find_element_by_xpath('//*[@id="indentifierNext"]/div/button/div [2 ]').click()

nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()

time.sleep(2)

driver.find_element_by_name("password").send_keys(pwd)

time.sleep(2)

# driver.find_element_by_xpath('//*[@id="indentifierNext"]/div/button/div [2 ]').click()
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()

time.sleep(3)

#To close the browser
driver.close()
print("Successful login to your account")
