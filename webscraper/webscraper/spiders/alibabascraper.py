import scrapy 


class AlibabaScraper(scrapy.Spider):
    name = 'alibaba'

    start_urls = ['https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=chair']

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