from dotenv import load_dotenv
load_dotenv(override=True)

from src.data import getCastDrivenData
from node import loader, splitter, embedder, retriever
from langchain_core.output_parsers import JsonOutputParser
from langchain_together import ChatTogether
from utils import prompts

llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf", temperature=0.4)

cast = 'KIM Ha Neul'
viu_datasets = "Viu_datasets"

def generating(use_case_data, retrieved_doc, push_number):
    
    input_variables = {
        "type_of_push_notification": "content-driven",
        "number_of_push_notifications": push_number,
        "name_of_series": use_case_data["series_name"],
        "retrieved_wiki_of_series": retrieved_doc,
        "series_description": use_case_data["series_description"],
        "name_of_cast": use_case_data["target_cast"],
        "type_of_cast": use_case_data["target_cast_type"],
        "nickname_of_cast": None,
        "quote_of_cast": None,
        "interesting_fact_of_cast": None,
        "retrieved_wiki_of_cast": retrieved_doc,
        "character_in_series_acted_by_cast": None,
        "demographics_of_target_receiver": "20-30 years old, fans of cast",
        "base_push_example": None,
        "local_trend_in_malaysia": "Viu is organizing an event inviting Kim Ha Nuel, Lin Tin Wai, and Rong Lam to Malaysia on June10, tickets are all sold out and people are very hyped to it.",
        "include_emoji": True,
        "include_slangs": True,
        "additional_requirements": None,
    }

    chain = prompts.final_prompt | llm | JsonOutputParser()

    push = chain.invoke(input_variables)
    
    print(push)


def testingPipeline(cast, push_number, datasets = "Viu_datasets"):
    
    print("___Start Handling Data___")
    cast_driven_data = getCastDrivenData(cast, datasets)
    
    print("___Start Loading___")
    series_wiki = loader.webLoading(cast_driven_data["series_wiki_url"])
    cast_wiki = loader.wikiLoading(cast)
    
    print("___Start Splitting___")
    splitted_wiki = splitter.splitting([series_wiki, cast_wiki])
    
    print("___Start Embedding___")
    series_vectorstore = embedder.embedding(splitted_wiki, cast)
    
    print("___Start Retrieval___")
    cast_retrieved_info = retriever.retrieving(series_vectorstore, cast, cast_driven_data["series_name"])
    
    print("___Start Generation___")
    generating(cast_driven_data, cast_retrieved_info, push_number)
    
    print("___End of Pipeline___")    

testingPipeline(cast, push_number = 5)