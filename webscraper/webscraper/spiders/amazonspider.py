import scrapy
import logging


class AmazonScraper(scrapy.Spider):
    name = 'amazon'

    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    start_urls = ['https://www.amazon.ca/s?k=brush&ref=nb_sb_noss']

    def parse(self, response):

        product_links = response.css('a.a-link-normal.s-no-outline::attr(href)').getall()

        for link in product_links:
            absolute_url = f'https://www.amazon.ca{link}'

            yield scrapy.Request(url=absolute_url, callback=self.parse_product)


        next_page_div = response.css('li.a-last')
        if next_page_div is not None:
            if response.css('li.a-last a::attr(href)').get() is not None:
                next_page_link = 'https://www.amazon.ca' + response.css('li.a-last a::attr(href)').get()
                yield response.follow(next_page_link,callback=self.parse)

    
    def parse_product(self,response):
        logging.info(response.url)

        yield {
            'Name' : response.css('span.a-size-large.product-title-word-break::text').get().replace('\n',''),
            'Description': response.xpath('//div[@id="productDescription"]/p/text()').get(),
            'Price': response.css('span.a-size-medium.a-color-price.priceBlockBuyingPriceString::text').get().replace('CDN$\xa0',''),
            'Rating': response.css('span.a-icon-alt::text').get().strip('out of 5 stars'),
            '# of Reviews': response.xpath('//span[@id="acrCustomerReviewText"]/text()').get().strip(' ratings'),
            'Link': response.url,
           # 'Image': ,
           # 'Supplier': ,

        }


