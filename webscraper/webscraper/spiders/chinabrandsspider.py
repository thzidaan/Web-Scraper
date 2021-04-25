import scrapy


class ChinabrandSpider(scrapy.Spider):
    name = 'chinabrands'

    def start_request(self):
        start_urls = [
            'https://www.chinabrands.com/dropshipping-xiaomi.html?searchUrl=%2Fsearch%2Fkeywords-notice.html&cat_id=&sid=209638585']

        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        all_products = response.css('ul.list-items')

        yield {
            'Name': all_products
        }

        yield
