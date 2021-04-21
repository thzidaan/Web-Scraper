import scrapy


class AmazonScraper(scrapy.Spider):
    name = 'amazon'

    start_urls = ['https://www.amazon.ca/s?k=brush&ref=nb_sb_noss_2']

    def parse(self, response):

        products = response.css('div.a-section.a-spacing-medium')

        for product in products:
            yield {
                'Name': product.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get(),
                'Price': product.css('span.a-offscreen::text').get().replace('$', ''),
                'Link': 'https://www.amazon.ca' + product.css('a.a-link-normal.a-text-normal').attrib['href']
            }


        next_page = response.css('n/a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)