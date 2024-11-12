from typing import Any

import scrapy
from scrapy.http import Response

#Used to scrape weirdkaya trending title
class Trend_Spider(scrapy.Spider):
    name = 'trend'
    start_urls = [
        'https://weirdkaya.com/tag/trending/'
    ]

    trend_title = []

    def parse(self, response):
        post_thumbs = response.css('.post-title::text').extract()
        self.trend_title = post_thumbs
        print("trend title: ", self.trend_title)
        yield self.trend_title
        # return self.trend_title








