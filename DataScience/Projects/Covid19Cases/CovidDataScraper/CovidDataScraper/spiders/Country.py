import scrapy


class CountrySpider(scrapy.Spider):
    name = 'Country'
    allowed_domains = ['worldometers.info']
    start_urls = ['http://worldometers.info/']

    def parse(self, response):
        pass
