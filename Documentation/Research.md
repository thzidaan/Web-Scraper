# Initial Research 

Scrapy Documentation. Link [here](https://docs.scrapy.org/en/latest/)

## First Problem

Scrapy was able to function but it could not scrape data from the sites which had dynamic rendering meaning it used javascript to load the page when an event occured such as scrolling. To counter that, I've decided to use scrapy-splash library which allows us to scrape through such websites.

### Splash Configuration in setting.py

```
ROBOTSTXT_OBEY = False

SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

## Second Problem 

Scrapy and Splash was neither unable to render pages that had javacript at the very beginning of the website, i.e none of the products would show up if javascript was being disabled in the browser. So a new library was used to tackle such cases. 

### Requests-HTML Library

For the given website [Aliexpress](https://www.aliexpress.com), the second problem first came to light. So no 'spider' was created for aliexpress, Instead the new library uses a different way to approach the problem. 

The library is able to create a 'fake' session which is then used to render the given website. Then using xpath and find function from the library, the necessary info was extracted from each of the websites. The problem that still persists is that the library is not able to produce all the products in a given page. It is able to scrape in around 28-32 products from site even though it shows the page itself contains around 40 products. 

#### Installation 

``` 
pip install request-html
```

