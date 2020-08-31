from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH = '/usr/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')


items = [driver.find_element_by_id('productPrice'+str(num)) for num in range(0, 2, 1)]

actions = ActionChains(driver)
actions.click(cookie)

try:
  for i in range(1000):
    actions.perform()
    count = int(cookie_count.text.split()[0])
    for item in items:
      value = int(item.text)
      if count >= value:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(item)
        upgrade_actions.click()
finally:
  driver.quit()

