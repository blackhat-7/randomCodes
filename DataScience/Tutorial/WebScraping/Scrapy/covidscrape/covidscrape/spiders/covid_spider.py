import scrapy


class PostsSpider(scrapy.Spider):
    name = 'table'
    start_urls = [
        'https://www.worldometers.info/world-population/india-population/'
    ]

    def parse(self, response):
        filename = 'table.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
