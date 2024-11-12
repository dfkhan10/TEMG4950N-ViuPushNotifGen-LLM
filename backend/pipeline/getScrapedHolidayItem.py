from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from utils.Scrapy_scraper.weirdkaya.spiders.holiday_spider import Holiday_Spider  # Import your spider



def run_holiday_spider():
    process = CrawlerProcess(get_project_settings())

    # Start the crawling process
    process.crawl(Holiday_Spider)

    # Start the process and wait for it to finish
    process.start()


    # print("scraped data: ", Holiday_Spider.date_holiday)

    return Holiday_Spider.date_holiday



