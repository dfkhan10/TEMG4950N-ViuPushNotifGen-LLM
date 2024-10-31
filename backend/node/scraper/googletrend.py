from dotenv import load_dotenv
load_dotenv(override=True)

import pandas as pd
from pytrends.request import TrendReq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.5)

def get_coutry_daily_trending(country):
    pytrends = TrendReq(hl='en-US', tz=480)
    data = pytrends.trending_searches(pn=country)
    return data

def trend_suggestion(trend_list, target):

    prompt = PromptTemplate(
        input_variables=["trend_list", "target"], 
        template="""
        Given the following list of marketing trends, classify each one based 
        on its suitability for use in push notification of a TV show. For example,
        For each trend, provide a very brief explanation of how it can be effectively used in 
        the promotion.

        Trend List (each trend seperated with ','): {trend_list}
        Content to be promoted: {target}

        Be sure to consider the show's genre, target audience, and overall brand 
        identity in your classifications and explanations.

        The output should be the desired trend to be used and corresponding usage.
        Discard the undesired one, keep consise and to the point.
    """)

    chain = prompt | llm | StrOutputParser()
    push = chain.invoke({"trend_list": {trend_list}, "target": {target}})
    print(push)

input = get_coutry_daily_trending('hong_kong').iloc[:,0].tolist()
input = ', '.join(input)
trend_suggestion(input, 'Korean Drama')
