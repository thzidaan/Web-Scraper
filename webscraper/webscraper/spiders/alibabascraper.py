import scrapy 
from scrapy_splash import SplashRequest


class AlibabaScraper(scrapy.Spider):
    name = 'alibaba'

    #start_urls = ['https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=chair']


    def start_requests(self):

        keyword = 'chair'

        domain = 'https://www.alibaba.com/products/' + keyword

        start_urls = [domain +'.html?IndexArea=product_en&page=1',
            domain +'.html?IndexArea=product_en&page=2',
            domain +'.html?IndexArea=product_en&page=3',
            domain +'.html?IndexArea=product_en&page=4',
            domain +'.html?IndexArea=product_en&page=5',
            domain +'.html?IndexArea=product_en&page=6',
            domain +'.html?IndexArea=product_en&page=7',
            domain +'.html?IndexArea=product_en&page=8',
            domain +'.html?IndexArea=product_en&page=9',
            domain +'.html?IndexArea=product_en&page=10',
            domain +'.html?IndexArea=product_en&page=11',
            domain +'.html?IndexArea=product_en&page=12',
            domain +'.html?IndexArea=product_en&page=13',
            domain +'.html?IndexArea=product_en&page=14',
            domain +'.html?IndexArea=product_en&page=15',
            domain +'.html?IndexArea=product_en&page=16',
            domain +'.html?IndexArea=product_en&page=17',
            domain +'.html?IndexArea=product_en&page=18',
            domain +'.html?IndexArea=product_en&page=19',
            domain +'.html?IndexArea=product_en&page=20',
            domain +'.html?IndexArea=product_en&page=21',
            domain +'.html?IndexArea=product_en&page=22',
            domain +'.html?IndexArea=product_en&page=23',
            domain +'.html?IndexArea=product_en&page=24',
            domain +'.html?IndexArea=product_en&page=25',
            domain +'.html?IndexArea=product_en&page=26',
            domain +'.html?IndexArea=product_en&page=27',
            domain +'.html?IndexArea=product_en&page=28',
            domain +'.html?IndexArea=product_en&page=29',
            domain +'.html?IndexArea=product_en&page=30',
            domain +'.html?IndexArea=product_en&page=31',
            domain +'.html?IndexArea=product_en&page=32',
            domain +'.html?IndexArea=product_en&page=33',
            domain +'.html?IndexArea=product_en&page=34',
            domain +'.html?IndexArea=product_en&page=35',
            domain +'.html?IndexArea=product_en&page=36',
            domain +'.html?IndexArea=product_en&page=37',
            domain +'.html?IndexArea=product_en&page=38',
            domain +'.html?IndexArea=product_en&page=39',
            domain +'.html?IndexArea=product_en&page=40',
            domain +'.html?IndexArea=product_en&page=41',
            domain +'.html?IndexArea=product_en&page=42',
            domain +'.html?IndexArea=product_en&page=43',
            domain +'.html?IndexArea=product_en&page=44',
            domain +'.html?IndexArea=product_en&page=45',
            domain +'.html?IndexArea=product_en&page=46',
            domain +'.html?IndexArea=product_en&page=47',
            domain +'.html?IndexArea=product_en&page=48',
            domain +'.html?IndexArea=product_en&page=49',
            domain +'.html?IndexArea=product_en&page=50',
            domain +'.html?IndexArea=product_en&page=51',
            domain +'.html?IndexArea=product_en&page=52',
            domain +'.html?IndexArea=product_en&page=53',
            domain +'.html?IndexArea=product_en&page=54',
            domain +'.html?IndexArea=product_en&page=55',
            domain +'.html?IndexArea=product_en&page=56',
            domain +'.html?IndexArea=product_en&page=57',
            domain +'.html?IndexArea=product_en&page=58',
            domain +'.html?IndexArea=product_en&page=59',
            domain +'.html?IndexArea=product_en&page=60',
            domain +'.html?IndexArea=product_en&page=61',
            domain +'.html?IndexArea=product_en&page=62',
            domain +'.html?IndexArea=product_en&page=63',
            domain +'.html?IndexArea=product_en&page=64',
            domain +'.html?IndexArea=product_en&page=65',
            domain +'.html?IndexArea=product_en&page=66',
            domain +'.html?IndexArea=product_en&page=67',
            domain +'.html?IndexArea=product_en&page=68',
            domain +'.html?IndexArea=product_en&page=69',
            domain +'.html?IndexArea=product_en&page=70',
            domain +'.html?IndexArea=product_en&page=71',
            domain +'.html?IndexArea=product_en&page=72',
            domain +'.html?IndexArea=product_en&page=73',
            domain +'.html?IndexArea=product_en&page=74',
            domain +'.html?IndexArea=product_en&page=75',
            domain +'.html?IndexArea=product_en&page=76',
            domain +'.html?IndexArea=product_en&page=77',
            domain +'.html?IndexArea=product_en&page=78',
            domain +'.html?IndexArea=product_en&page=79',
            domain +'.html?IndexArea=product_en&page=80',
            domain +'.html?IndexArea=product_en&page=81',
            domain +'.html?IndexArea=product_en&page=82',
            domain +'.html?IndexArea=product_en&page=83',
            domain +'.html?IndexArea=product_en&page=84',
            domain +'.html?IndexArea=product_en&page=85',
            domain +'.html?IndexArea=product_en&page=86',
            domain +'.html?IndexArea=product_en&page=87',
            domain +'.html?IndexArea=product_en&page=88',
            domain +'.html?IndexArea=product_en&page=89',
            domain +'.html?IndexArea=product_en&page=90',
            domain +'.html?IndexArea=product_en&page=91',
            domain +'.html?IndexArea=product_en&page=92',
            domain +'.html?IndexArea=product_en&page=93',
            domain +'.html?IndexArea=product_en&page=94',
            domain +'.html?IndexArea=product_en&page=95',
            domain +'.html?IndexArea=product_en&page=96',
            domain +'.html?IndexArea=product_en&page=97',
            domain +'.html?IndexArea=product_en&page=98',
            domain +'.html?IndexArea=product_en&page=99',
            domain +'.html?IndexArea=product_en&page=100',

]
        for url in start_urls:
            yield SplashRequest(url, callback=self.parse)

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

        