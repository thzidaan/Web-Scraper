import scrapy


class AliexpressScraper(scrapy.Spider):
    name = 'aliexpress'

    start_urls = ['']

    def parse(self, response):

        yield 








