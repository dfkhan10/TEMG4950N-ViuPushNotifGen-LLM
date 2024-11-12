from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from utils.Scrapy_scraper.weirdkaya.spiders.Trend_spider import Trend_Spider

    

def run_weirdkaya_trend_spider():
    process = CrawlerProcess(get_project_settings())


    # Start the crawling process
    process.crawl(Trend_Spider)


    # Start the process and wait for it to finish
    process.start()


    # print("scraped data: ", Trend_Spider.trend_title)
    return Trend_Spider.trend_title

    