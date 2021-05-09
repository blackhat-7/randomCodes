import scrapy
from scrapy.http import Request
from NewsScraperScrapy.items import NewsscraperscrapyItem
import os
import json
from datetime import datetime


class ArticlecontentSpider(scrapy.Spider):
    name = 'ArticleContent'
    allowed_domains = ['energy.gov']
    start_urls = ['http://energy.gov/']

    def start_requests(self):
        with open(os.getcwd() + '/article_urls.json') as json_file:
            articles = json.load(json_file)
            for a in articles:
                request = Request(a['article_url'], meta={'url': a['article_url']}, callback=self.parse_content)
                yield request

    def parse_content(self, response):
        item = NewsscraperscrapyItem()
        date = response.xpath('//div[@class="page-hero-date"]/text()').extract_first()
        item['article_date'] = datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
        item['article_title'] = response.xpath('//h1[@class="page-title"]/text()').extract_first().strip('\n').strip()
        item['article_url'] = response.meta['url']
        item['article_description'] = ' '.join(response.xpath('//div[@class="block block-layout-builder block-inline-blockbasic"]//p//text()').extract())
        yield(item)

    def parse(self, response):
        pass
