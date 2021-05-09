# import selenium drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import pandas as pd
from datetime import datetime
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from time import time


class NewsScraper():
    '''Class to scrape news articles from "www.energy.gov"
    '''

    def __init__(self, webdriver_path: str, headless: bool, num_pages: int, save_path: str, url: str, delay: int):
        '''
        Parameters
        ----------
        webdriver_path: str, path to chrome webdriver
        headless: bool, whther to run the scraper headlessly
        num_pages: int, number of pages to scrape
        save_path: str, dataset save location (include file name)
        url: str, url to start scraping from
        delay: int, number of seconds to wait for page to load
        '''
        # check parameter types
        if type(webdriver_path) != str or type(headless) != bool or type(num_pages) != int or type(save_path) != str or type(url) != str or type(delay) != int:
            print("Type Error: Invalid type in arguements")
            exit(0)
        if not os.path.exists(webdriver_path):
            print('Webdriver not found')
            exit(0)

        self.webdriver_path = webdriver_path
        self.headless = headless
        self.num_pages = num_pages
        self.save_path = save_path
        self.url = url
        self.delay = delay

    def init_record(self) -> dict:
        return {'article_date': None, 'article_title': None, 'article_description': '', 'article_url': None}

    def wait_for_element(self, classname: str) -> bool:
        try:
            element_present = EC.presence_of_element_located(
                (By.CSS_SELECTOR, classname))
            WebDriverWait(self.driver, self.delay).until(element_present)
        except TimeoutException:
            print("Timed out waiting for element")
            return False
        return True

    def get_news_urls(self, page: int) -> list:
        if not self.wait_for_element('.search-result-title'):
            return []
        articles = self.driver.find_elements_by_css_selector(
            '.search-result-title')
        articles = [a.get_property('href') for a in articles]
        print(f'Page: {page+1}    Num articles: {len(articles)}')
        return articles

    def make_url_clickable(self, url: str) -> str:
        return f'<a href="{url}">{url}</a>'

    def get_record(self, article: str) -> dict:
        record = self.init_record()
        if not self.wait_for_element('.page-hero-date'):
            return record

        date = self.driver.find_element_by_css_selector('.page-hero-date').text
        record['article_date'] = datetime.strptime(
            date, '%B %d, %Y').strftime('%Y-%m-%d')
        record['article_title'] = self.driver.find_element_by_css_selector(
            '.page-title').text
        record['article_url'] = article
        desc = self.driver.find_element_by_css_selector(
            'div.block.block-layout-builder.block-inline-blockbasic')
        record['article_description'] += desc.find_element_by_tag_name(
            'p').text
        return record

    def save_data(self, data: list) -> None:
        df = pd.DataFrame(data)
        df.style.format(self.make_url_clickable, subset=['article_url'])
        df.to_excel(self.save_path, index=False)
        print('Data saved successfully.')

    def scrape(self) -> None:
        start = time()
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(self.webdriver_path, options=options)

        data = []

        try:
            # For each page
            self.driver.get(self.url)
            for i in range(self.num_pages):
                cur_url = self.driver.current_url
                articles = self.get_news_urls(i)
                # For each article
                for article in articles:
                    # Open article
                    self.driver.get(article)

                    # Get details
                    data.append(self.get_record(article))

                self.driver.get(cur_url)
                if not self.wait_for_element('li.pagination-item.pagination-next'):
                    break
                self.driver.find_element_by_css_selector(
                    'li.pagination-item.pagination-next').click()
                if self.driver.current_url == cur_url:
                    print('No more articles found')
                    break
        finally:
            # Close the webdriver
            self.driver.quit()

        print(f'Total articles scraped: {len(data)}')
        self.save_data(data)
        print(f'Time elapsed: {(time()-start): .2f} seconds')


def create_word_cloud(save_path):
    df = pd.read_excel(save_path)
    text = ''
    for news in df.article_description.tolist():
        tokens = word_tokenize(str(news))
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        text += ' '.join(tokens) + ' '

    wordcloud = WordCloud(width=2000, height=2000,
                          stopwords=set(STOPWORDS)).generate(text)

    # plot the WordCloud image
    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


if __name__ == '__main__':
    # Constants and Parameters
    URL = 'https://www.energy.gov/listings/energy-news'
    DRIVER_PATH = os.getcwd() + '/chromedriver'
    SAVE_PATH = './energygov_selenium.xlsx'
    HEADLESS = True
    NUM_PAGES = 10
    DELAY = 2

    ns = NewsScraper(DRIVER_PATH, HEADLESS, NUM_PAGES, SAVE_PATH, URL, DELAY)
    ns.scrape()

    # Comment this if you don't want to plot wordcloud
    create_word_cloud(SAVE_PATH)
