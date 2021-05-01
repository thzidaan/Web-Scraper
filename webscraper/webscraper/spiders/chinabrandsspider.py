import scrapy
from scrapy_splash import SplashRequest


class ChinabrandsSpider(scrapy.Spider):
    name = 'chinabrands'

    def start_request(self):
        start_urls = [
            'https://www.chinabrands.com/dropshipping-headphones.html?searchUrl=%2Fsearch%2Fkeywords-notice.html&cat_id=']

        for url in start_urls:
            yield SplashRequest(url, callback=self.parse)

    def parse(self, response):

        all_products = response.css('ul.clearfix')
        for product in all_products:

            absolute_url = product.xpath('//*[@id="pro-list"]/ul/li[1]/div[3]/a').attrib['href']

            yield SplashRequest(url=absolute_url, callback=self.parse_product)

        
    def parse_product(self,response): 

        yield {

            'Name' : response.css('h3.goods-title.f18.mb15').attrib['title'],
            #'Description': ,
            'Price': response.css('span.my_shop_price.fb').attrib['data-orgp'],
           # 'Rating': ,
           # '# of Reviews': ,
            'Link': response.url,
        }

