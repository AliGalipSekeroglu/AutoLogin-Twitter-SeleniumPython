from selenium import webdriver
import twitterInfo #Importing the file which contains our Twitter password and username.
import time

browser = webdriver.Firefox()

url ="https://twitter.com/"
browser.get(url)

time.sleep(3)

#We can get those Xpaths when we click something on any item's of Twitter
#Right click->Inspect->Find the item on Elements -> Right click ->Copy -> Copy XPath

log_in = browser.find_element_by_xpath ("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
log_in.click()

time.sleep(3)

username=browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password=browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

username.send_keys(twitterInfo.username) #Sending datas from twitterInfo.py to here.
password.send_keys(twitterInfo.password) #Sending datas from twitterInfo.py to here.
time.sleep(3)

log_in_button = browser.find_element_by_xpath ("//*[@id='page-container']/div/div[1]/form/div[2]/button")
log_in_button.click()

time.sleep(15)

browser.close()
