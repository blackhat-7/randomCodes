from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "/usr/bin/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

link = driver.find_element_by_link_text("Game Development With Python")
link.click()


try:
    video_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT))
    )
    video_link.click()
except:
    driver.quit()

