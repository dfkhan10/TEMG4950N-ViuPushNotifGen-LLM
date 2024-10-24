from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
from fastapi.responses import JSONResponse
from model.push_notification import PushResponse
from pipeline import castDrivenPipeline

cast_driven_router = APIRouter()

@cast_driven_router.post("/genPush")
async def gen_push(cast_name: Optional[str]) -> PushResponse:
   try:
      print("---testing---")
      eng_push, malay_push = castDrivenPipeline(cast_name)
      return PushResponse(eng_push=eng_push, malay_push=malay_push)
   except Exception as e:
      print(e)
      raise e