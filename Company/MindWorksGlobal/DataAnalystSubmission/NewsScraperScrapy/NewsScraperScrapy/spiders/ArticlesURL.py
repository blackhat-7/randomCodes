import scrapy
from scrapy.http import Request
from NewsScraperScrapy.items import NewsscraperscrapyItem


class ArticlesurlSpider(scrapy.Spider):
    name = 'ArticlesURL'
    allowed_domains = ['energy.gov']
    start_urls = ['https://www.energy.gov']

    def start_requests(self):
        url = 'https://www.energy.gov/listings/energy-news?page={}'
        all_urls = [url.format(i) for i in range(5)]
        for url in all_urls:
            request = Request(url, callback=self.parse_page)
            yield request

    def parse_page(self, response):
        item = NewsscraperscrapyItem()
        content = response.xpath('//a[@class="search-result-title"]')
        for article in content:
            href = article.xpath('.//@href').extract_first()
            item['article_url'] = 'https://www.energy.gov' + href
            yield item

    def parse(self, response):
        pass
