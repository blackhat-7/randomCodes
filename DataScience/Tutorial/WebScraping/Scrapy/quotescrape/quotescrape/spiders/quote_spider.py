from quotescrape.items import QuotescrapeItem
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        quotes = response.css('div.quote')
        item = QuotescrapeItem()
        for quote in quotes:
            item['quote'] = quote.css('span.text::text')[0].extract()
            item['author'] = quote.css('small.author::text')[0].extract()
            item['tags'] = quote.css('a.tag::text').extract()
            yield item

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

        next_page = 'http://quotes.toscrape.com/page/' + str(self.page_number) + '/'
        if self.page_number < 11:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)
