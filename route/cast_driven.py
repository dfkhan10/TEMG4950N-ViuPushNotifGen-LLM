from fastapi import APIRouter
from typing import Optional, Dict
from model.push_notification import PushResponse
from pipeline import castDrivenPipeline

cast_driven_router = APIRouter()

@cast_driven_router.post("/genPush")
async def gen_push(cast_name: Optional[str]) -> Dict[int, PushResponse]:
   try:
      print("---testing---")
      pushes = castDrivenPipeline(cast_name, push_number = 5)
      return pushes
   except Exception as e:
      print(e)
      raise e