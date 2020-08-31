import requests
from bs4 import BeautifulSoup as bs

url = 'https://keithgalli.github.io/web-scraping/'

r = requests.get(url + 'webpage.html')
webpage = bs(r.content, 'lxml')


images = webpage.select('div.row div.column img')
image_urls = [url + image['src'] for image in images]

for i, url in enumerate(image_urls):
    img_data = requests.get(url).content
    with open('image'+str(i), 'wb') as handler:
        handler.write(img_data)
print('All images have been saved.')
