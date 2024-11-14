from dotenv import load_dotenv

load_dotenv(override=True)

# cast = 'KIM Ha Neul'
# viu_datasets = "Viu_datasets"

# # from pipeline.pipeline import castDrivenPipeline
# # castDrivenPipeline(cast, push_number = 5)

# from pipeline import genPush
# genPush.testingPipeline(cast, push_number = 5)

# # from pipeline.pipeline import contentDrivenPipeline
# # contentDrivenPipeline('Nothing Uncovered', push_number = 5)

# # from pipeline import genPush
# # genPush.testingContentPipeline('Nothing Uncovered', push_number = 5)

#Test for spider
from pipeline.getScrapedHolidayItem import run_holiday_spider
from pipeline.getSrapedTrendItem import run_weirdkaya_trend_spider
from pipeline.getScrapedItem import run_spiders
from pipeline.getAllScrapedItem import run_all_spiders
from pipeline.getScrapedWarningItem import run_weather_warning_spider
from node.Holiday_classifier import check_holiday_status
if __name__ == "__main__":
    # scraped_data1 = run_holiday_spider()
    # scraped_data2 = run_weirdkaya_trend_spider()
    # print("main scraped data1: ", scraped_data1)
    # scraped_data1, scraped_data2 = run_spiders()
    # print("main scraped data2: ", scraped_data2)

    scraped_data = run_all_spiders()
    # print(scraped_data)
    holiday_dict = scraped_data['holidays']
    trend_title = scraped_data['trends']['trend']
    Today_holiday, Upcoming_holiday, Error_holiday = check_holiday_status(holiday_dict)
    print(Today_holiday, Upcoming_holiday, Error_holiday)
    # print("main scraped data:")
    # print("hodidays: ")
    # print(holiday_dict)
    # print("trend: ")
    # print(trend_title)

    # run_weather_warning_spider()



#Test for thumbnails
# from node.thumbnails import retrieve_thumbnail

# if __name__ == "__main__":
#     thumbnails_retrieved = retrieve_thumbnail("060ac139-fae3-4c2b-84bc-f0c3af0b56a1", "D:/Viu_data/series_thumbnails/series_thumbnails")
#     print(thumbnails_retrieved)

# from node.thumbnails import retrieve_thumbnail
# if __name__ == "__main__":
#     thumbnails_retrieved = retrieve_thumbnail("060ac139-fae3-4c2b-84bc-f0c3af0b56a1", "D:/Viu_data/series_thumbnails/series_thumbnails")
#     for img in thumbnails_retrieved:
#         img.show()

