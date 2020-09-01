from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def print_news(headlines):
  for i, headline in enumerate(headlines):
    print('Headline ' + str(i) + ": " + headline)

def get_news(search_key: str):
  key = '+'.join(search_key.split(' '))
  url = 'https://www.google.com/search?q=' + key + '&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjugqqgisbrAhUO1hoKHeA1A8kQ_AUoBHoECBcQBg"'

  driver = webdriver.Chrome()
  driver.get(url)
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser') 
  
  headlines = []
  for _ in range(3):
    head = soup.find_all('div', attrs={ 'class': 'JheGif nDgy9d' })
    headlines += [h.text for h in head]
    next_btn = driver.find_element_by_id('pnnext')
    mouse_action = ActionChains(driver)
    mouse_action.click(next_btn)
    mouse_action.perform()
    driver.implicitly_wait(2)
  print_news(headlines)



def main():
  search_key = input()
  get_news(search_key)

if __name__ == "__main__":
    main()

'''
session[username_or_email]
session[password]

show more
css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0

css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0

'''
