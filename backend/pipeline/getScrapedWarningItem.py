from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from utils.Scrapy_scraper.weirdkaya.spiders.Weather_spider import weather_Spider  # Import your spider



def run_weather_warning_spider():
    process = CrawlerProcess(get_project_settings())

    # Start the crawling process
    process.crawl(weather_Spider)

    # Start the process and wait for it to finish
    process.start()


    # print("scraped data: ", Holiday_Spider.date_holiday)

    # return Holiday_Spider.date_holiday



