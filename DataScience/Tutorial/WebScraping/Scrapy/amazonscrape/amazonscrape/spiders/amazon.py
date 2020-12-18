from amazonscrape.items import AmazonscrapeItem
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_nav_0/']

    def parse(self, response):
        item = AmazonscrapeItem()
        books = response.css('.aok-relative')
        for book in books:
            item['name'] = book.css('.p13n-sc-truncate-desktop-type2::text').get().replace('\n', '').strip()
            author = book.css('.a-link-child::text').get()
            if not author:
                author = book.css('.a-color-base::text').get()
            item['author'] = author
            item['image'] = book.css('.a-spacing-small img::attr(src)').get()
            item['price'] = book.css('.p13n-sc-price::text').get()
            yield item
        next_page = response.css('.a-last a::attr(href)').extract()
        print(next_page)
        if next_page:
            yield response.follow(next_page[0], callback=self.parse)
