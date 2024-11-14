from typing import Any

import scrapy
from scrapy.http import Response

#Used to scrape weirdkaya trending title
class weather_Spider(scrapy.Spider):
    name = 'weather'
    start_urls = [
        'https://www.met.gov.my/en/'
    ]

    def parse(self, response):
        warnings = response.css('h6::text').extract()

        warning_blocks = response.css('.bg-white.text-center.rounded-lg.py-5.px-8')
        links = []
        for block in warning_blocks:
            link = block.css('a::attr(href)').get()
            if link:
                full_link = response.urljoin(link)
            links.append(link)

        
        yield {"warnings" : warnings, "links": links}


# class weather_Spider(scrapy.Spider):
#     name = 'weather'
#     start_urls = [
#         'https://publicinfobanjir.water.gov.my/ramalan/met-alert/?lang=en'
#     ]

#     def parse(self, response):





