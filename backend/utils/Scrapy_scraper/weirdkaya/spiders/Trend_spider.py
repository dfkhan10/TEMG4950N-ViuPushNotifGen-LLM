from typing import Any

import scrapy
from scrapy.http import Response

#Used to scrape weirdkaya trending title
class Trend_Spider(scrapy.Spider):
    name = 'trend'
    start_urls = [
        'https://weirdkaya.com/tag/trending/'
    ]

    def parse(self, response):
        post_thumbs = response.css('.post-title::text').extract()
        yield {"trend": post_thumbs}








