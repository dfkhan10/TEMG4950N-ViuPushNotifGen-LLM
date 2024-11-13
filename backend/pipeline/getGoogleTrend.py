from dotenv import load_dotenv
load_dotenv(override=True)

from pytrends.request import TrendReq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

def get_coutry_daily_trending(country='malaysia'):

    pytrends = TrendReq(hl='en-US', tz=480)
    data = pytrends.trending_searches(pn=country)
    return data

def get_trend_search(trend):

    wrapper = DuckDuckGoSearchAPIWrapper(region="my-en", time="d", max_results=2) # my-en = Malaysia English my-ms = Malaysia Malay
    search = DuckDuckGoSearchResults(api_wrapper=wrapper, output_format="list")

    result = search.invoke(trend)

    #print(result)
    return result

# input = get_coutry_daily_trending('malaysia').iloc[:,0].tolist()

# print(get_trend_search('Song Jae Rim'))