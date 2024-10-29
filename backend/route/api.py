from fastapi import APIRouter
from typing import Optional, Dict
from utils.schema import PushResponse
from pipeline.pipeline import castDrivenPipeline
from src import data

api_router = APIRouter()

@api_router.get("/viuData")
async def get_viu_data() -> dict:
   try:
      return {"key": "value"}
   except Exception as e:
      print(e)
      raise e

@api_router.post("/genPush")
async def gen_push(cast_name: Optional[str]) -> Dict[int, PushResponse]:
   try:
      print("---testing---")
      pushes = castDrivenPipeline(cast_name, push_number = 5)
      return pushes
   except Exception as e:
      print(e)
      raise e