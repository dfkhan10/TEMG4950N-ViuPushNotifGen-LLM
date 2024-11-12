from dotenv import load_dotenv

load_dotenv(override=True)

import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route.api import api_router
from src.data import getMalayData

app = FastAPI()

malayData = getMalayData("Viu_datasets")
backendState = {
    "type_of_push_notification": None,
    "number_of_push_notifications": 5,
    "name_of_series": None,
    "retrieved_wiki_of_series": None,
    "series_content": None, 
    "series_description": None,
    "name_of_cast": None,
    "type_of_cast": None,
    "nickname_of_cast": None,
    "quote_of_cast": None,
    "interesting_fact_of_cast": None,
    "character_in_series_acted_by_cast": None,
    "creativity": 0.2,
    "demographics_of_target_receiver": [0, 100],
    "base_push_example": None,
    "local_trend_in_malaysia": None,
    "include_emoji": True,
    "include_slangs": True,
    "additional_requirements": None,
    "supporting_documents": None,
    "pushes": None,
}

app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = [os.getenv("FRONTEND_URL")], 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

if __name__ == "__main__":
    uvicorn.run(app)