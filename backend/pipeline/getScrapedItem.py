from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from utils.Scrapy_scraper.weirdkaya.spiders.holiday_spider import Holiday_Spider
from utils.Scrapy_scraper.weirdkaya.spiders.Trend_spider import Trend_Spider

class DataCapture:
    def __init__(self):
        self.data = []

    def capture_data(self, item, response, spider):
        self.data.append(item)
        return item

def run_spiders():
    data_capture_holiday = DataCapture()
    data_capture_trend = DataCapture()

    process = CrawlerProcess(get_project_settings())

    # Start the crawling process for both spiders
    process.crawl(Holiday_Spider, item=data_capture_holiday.capture_data)
    process.crawl(Trend_Spider, item=data_capture_trend.capture_data)

    # Start the process and wait for it to finish
    process.start()

    return data_capture_holiday.data, data_capture_trend.data

# if __name__ == "__main__":
#     scraped_data1, scraped_data2 = run_spiders()
#     print("main scraped data1: ", scraped_data1)
#     print("main scraped data2: ", scraped_data2)