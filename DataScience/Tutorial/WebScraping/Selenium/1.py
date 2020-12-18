from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()

browser.implicitly_wait(10)

browser.get("http://google.com/")

browser.quit()
