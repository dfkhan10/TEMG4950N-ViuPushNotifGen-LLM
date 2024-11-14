from typing import Any

import scrapy
from scrapy.http import Response

#Used to get holiday data
# class Holiday_Spider(scrapy.Spider):
#     name = 'holiday'
#     start_urls = [
#         'https://ecentral.my/public-holiday-2024/'
#     ]

#     def parse(self, response):
#         # Select all <tr> elements in the table body
#         rows = response.css('tbody tr')

#         # Initialize an empty list to hold the dates
#         date_holiday = {}

#         for row in rows:
#             # Extract the date from the first <td> in each row
#             date = row.css('td::text').get()  # Get the first <td> text
#             holiday_name = row.css('td:nth-of-type(2)::text').get()
#             if date:  # Check if date is not None
#                 date_holiday[date.strip()] = holiday_name.strip()  # Strip any extra whitespace

#         yield {'Holidays': date_holiday}  # Yield the dictionary of dates

# def dummy():
#     Holiday_Spider()

class Holiday_Spider(scrapy.Spider):
    name = 'holiday'
    start_urls = [
        'https://ecentral.my/public-holiday-2024/'
    ]
    # Initialize an empty list to hold the dates
    date_holiday = {}

    def parse(self, response):
        # Select all <tr> elements in the table body
        rows = response.css('tbody tr')

        for row in rows:
            # Extract the date from the first <td> in each row
            date = row.css('td::text').get()  # Get the first <td> text
            holiday_name = row.css('td:nth-of-type(2)::text').get()
            if date:  # Check if date is not None
                self.date_holiday[date.strip()] = holiday_name.strip()  # Strip any extra whitespace

        yield self.date_holiday  # Yield the dictionary of dates







