import scrapy


class MacbookSpider(scrapy.Spider):
    name = 'Macbook'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
