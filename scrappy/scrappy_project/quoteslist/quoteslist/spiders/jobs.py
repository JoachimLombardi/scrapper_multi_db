# https://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/#Scrapy_Tutorial_Getting_Started
# scrapy crawl jobs

import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            quote_ = {"quote": quote.xpath('.//*[@class="text"]/text()').get(),
                      # Pour être resilien au changement on met des * et
                      # non le nom des balises
                      "author": quote.xpath(
                         './/*[@class="author"]/text()').get()}

            yield quote_
        relative_urls = response.xpath('//*[@class="next"]/a/@href')
        if relative_urls:
            yield from response.follow_all(relative_urls, self.parse)
            # Pour le faire page par page
