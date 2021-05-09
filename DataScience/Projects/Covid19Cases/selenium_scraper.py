# import selenium drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import pandas as pd
from time import time
import re


class Covid19Scraper():
    '''Class to scrape covid data from "https://www.worldometers.info/coronavirus/#main_table"
    '''

    def __init__(self, webdriver_path: str, headless: bool, save_path: str, url: str, delay: int):
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
        if type(webdriver_path) != str or type(headless) != bool or type(save_path) != str or type(url) != str or type(delay) != int:
            print("Type Error: Invalid type in arguements")
            exit(0)
        if not os.path.exists(webdriver_path):
            print('Webdriver not found')
            exit(0)

        self.webdriver_path = webdriver_path
        self.headless = headless
        self.save_path = save_path
        self.url = url
        self.delay = delay

    def wait_for_element(self, classname: str) -> bool:
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, classname))
            WebDriverWait(self.driver, self.delay).until(element_present)
        except TimeoutException:
            print("Timed out waiting for element")
            return False
        return True

    def clean_data(self, df):
        print('Cleaning data')
        num_cols = list(df.columns)
        num_cols.remove('region')

        for idx, row in df.iterrows():
            for col in num_cols:
                if row[col] is not None:
                    row[col] = re.sub(r'[^\d]+', '', str(row[col]))
                    df.loc[idx, col] = int(row[col]) if row[col].isdigit() else None
        return df

    def save_data(self, data: list) -> None:
        df = pd.DataFrame(data)
        df = self.clean_data(df)
        print('Saving data')
        df.to_csv(self.save_path, index=False)
        print('Data saved successfully.')

    def scrape(self) -> None:
        print('Scraping Data')
        start = time()
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(self.webdriver_path, options=options)

        data = []

        try:
            self.driver.get(self.url)
            self.wait_for_element('a.mt_a')
            rows = self.driver.find_elements_by_xpath('//tr[@role="row"]')
            print(len(rows))
            for row in rows:
                cols = row.find_elements_by_xpath('.//td')
                if len(cols) >= 5 and cols[1].text != '':
                    record = {}
                    record['region'] = cols[1].text
                    record['total_cases'] = cols[2].text
                    record['total_deaths'] = cols[4].text
                    record['total_recovered'] = cols[6].text
                    record['active_cases'] = cols[7].text
                    record['total_cases/1M_population'] = cols[9].text
                    record['deaths/1M_population'] = cols[10].text
                    record['total_tests'] = cols[11].text
                    record['tests/1M_population'] = cols[12].text
                    record['population'] = cols[13].text
                    data.append(record)

        finally:
            # Close the webdriver
            self.driver.quit()

        self.save_data(data)
        print(f'Time elapsed: {(time()-start): .2f} seconds')


if __name__ == '__main__':
    # Constants and Parameters
    URL = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?'
    DRIVER_PATH = os.getcwd() + '/chromedriver'
    SAVE_PATH = './covid19_data.csv'
    HEADLESS = True
    NUM_PAGES = 10
    DELAY = 2

    cs = Covid19Scraper(DRIVER_PATH, HEADLESS, SAVE_PATH, URL, DELAY)
    cs.scrape()
