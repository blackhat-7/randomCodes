import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import time
import schedule

URL = 'https://www.amazon.com/Apple-MacBook-Quad-Core-Z0W40LL-Exclusive/dp/B083TNTDPK/ref=sr_1_7?dchild=1&keywords=macbook+pro&qid=1598947254&s=electronics&sr=1-7'


def get_price():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.implicitly_wait(5)

    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')
    price = None
    try:
        print("Product:")
        title = soup.find(id="productTitle").get_text().strip()
        print(title)
        print("\nPrice:")
        price = soup.find(id="price_inside_buybox").get_text().strip()
        print(price)
    finally:
        driver.quit()
    if price != None:
        price = float(price[1:].replace(',', ''))
    return price


def send_mail():
    my_mail = "shaunak18098@iiitd.ac.in"
    wanted_price = 1_000
    psswd = 'kvnkpfdxkmakcxxh'
    current_price = get_price()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('shaunak18098@iiitd.ac.in', psswd)
    if current_price is not None:
        if current_price < wanted_price:
            subject = f"Price of Macbook Pro 2019 256GB below ${wanted_price}!"
        else:
            subject = f"Price of Macbook Pro 2019 256GB above ${wanted_price}"
        body = f"Current Price: ${current_price}\nWanted Price: ${wanted_price}\nCheck on Amazon:\n {URL}"

        message = f"Subject: {subject}\n\n{body}"
    
        server.sendmail(
            my_mail,
            my_mail,
            message
        )
        print("Mail has bee sent!")
    else:
        server.sendmail(my_mail, my_mail, "Subject: Error: current_price is None\n\nDebug ~/DataScience/Tutorial/WebScraping/AmazonPrices/AmazonPrices.py")
    server.quit()


schedule.every().day.at("18:01").do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(86400)


