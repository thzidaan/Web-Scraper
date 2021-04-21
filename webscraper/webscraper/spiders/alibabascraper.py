import scrapy 
from scrapy_splash import SplashRequest


class AlibabaScraper(scrapy.Spider):
    name = 'alibaba'

    #start_urls = ['https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=chair']

    def start_requests(self):

        #url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=chair'
        url = 'https://www.alibaba.com/products/chair.html?IndexArea=product_en&page=10'

        yield SplashRequest(url)

    def parse(self, response):

        products = response.css('div.organic-offer-wrapper.organic-gallery-offer-inner.m-gallery-product-item-v2.img-switcher-parent')

        for product in products:
            yield {
                'Name': product.css('p.elements-title-normal__content.medium::text').get(),
                'Price': product.css('span.elements-offer-price-normal__price::text').get(),
                'Supplier': product.css('a.organic-gallery-offer__seller-company::text').get(),
                'Rating (Stars)': product.css('span.seb-supplier-review__score::text').get(),
                'Link': products.css('a.organic-gallery-offer__img-section').attrib['href'],
                
            }