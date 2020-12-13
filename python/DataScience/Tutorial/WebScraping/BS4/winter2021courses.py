from bs4 import BeautifulSoup as bs
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
try:
    browser = webdriver.Safari()
    browser.get('http://techtree.iiitd.edu.in')
    time.sleep(2)
    soup = bs(browser.page_source, 'lxml')
    th = [th.get_text() for th in soup.find('thead').find_all('th')[1:]]
    table = [[td.get_text() for td in tr.find_all('td')[1:]] for tr in soup.find('tbody').find_all('tr')]
    table.insert(0, th)
    for row in table[:5]:
        print(*row)
    with open('winter2021courses.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(table)
        print('File saved!')

finally:
    browser.quit()
