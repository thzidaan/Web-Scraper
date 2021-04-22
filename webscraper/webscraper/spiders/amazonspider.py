import scrapy


class AmazonScraper(scrapy.Spider):
    name = 'amazon'

    start_urls = ['https://www.amazon.ca/s?k=brush&qid=1619045877&ref=sr_pg_1']

    def parse(self, response):

        products = response.css('div.a-section.a-spacing-medium')

        for product in products:

            if product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get() is not None and product.css('span.a-offscreen::text').get() is not None and product.css('a.a-link-normal.a-text-normal').attrib['href'] is not None :
                yield {
                    'Name': product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get(),
                    'Price': product.css('span.a-offscreen::text').get().replace('$', ''),
                    'Link': 'https://www.amazon.ca' + product.css('a.a-link-normal.a-text-normal').attrib['href']
                }


        next_page_div = response.css('li.a-last')
        if next_page_div is not None:
            if response.css('li.a-last a::attr(href)').get() is not None:
                next_page_link = 'https://www.amazon.ca' + response.css('li.a-last a::attr(href)').get()
                yield response.follow(next_page_link,callback=self.parse)