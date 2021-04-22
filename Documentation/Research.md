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