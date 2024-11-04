from fastapi import APIRouter, UploadFile
from typing import Optional, Dict, List
from utils.schema import PushRequest, PushResponse
from pipeline.pipeline import castDrivenPipeline
from src import data

api_router = APIRouter()

@api_router.get("/viuData")
async def get_viu_data() -> dict:
   from main import malayData
   try:
      return malayData.to_dict(orient='records')
   except Exception as e:
      print(e)
      raise e

@api_router.get("/thumbnails")
async def get_viu_data() -> List[UploadFile]:
   try:
      return None ## return get thumbnails
   except Exception as e:
      print(e)
      raise e

@api_router.post("/scrapeTrends")
async def gen_push(cast_name: Optional[str], series_name: Optional[str]) -> dict:
   try:
      # scrape trend function
      # return pushes
      return {}
   except Exception as e:
      print(e)
      raise e

@api_router.post("/genPush")
async def gen_push(input_data: PushRequest) -> Dict[int, PushResponse]:
   try:
      from main import backendState
      backendState["type_of_push_notification"] = input_data.push_type
      backendState["name_of_series"] = input_data.series_name
      backendState["name_of_cast"] = input_data.cast_name
      backendState["creativity"] = input_data.creativity
      backendState["demographics_of_target_receiver"] = input_data.demographics
      backendState["include_emoji"] = input_data.isEmojis
      backendState["include_slangs"] = input_data.isSlangs
      backendState["additional_requirements"] = input_data.addRequirements
      backendState["supporting_documents"] = input_data.otherSupportingDocuments
      
      pushes = castDrivenPipeline("Kim Ha-Nuel", push_number = 5)
      return pushes
   
   except Exception as e:
      print(e)
      raise e
   
@api_router.post("/regenPush")
async def regen_push(base_push: PushResponse, additional_requirements: Optional[str]) -> Dict[int, PushResponse]:
   try:
      from main import backendState
      backendState["additional_requirements"] = additional_requirements
      
      pushes = None ##regen function using base_push and additional requirements
      return pushes
   
   except Exception as e:
      print(e)
      raise e