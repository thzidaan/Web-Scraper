import scrapy
from scrapy_splash import SplashRequest


class AliexpressScraper(scrapy.Spider):
    name = 'aliexpress'

   

    def start_request(self):
        start_urls = ['https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=chair&ltype=wholesale&SortType=default&page=1']

        for url in start_urls:
            yield SplashRequest(url, callback=self.parse)


    def parse(self, response):

        all_products = response.css('ul.list-items')

        yield {
            'Name': all_products
        }         

        yield 








