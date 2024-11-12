from pydantic import BaseModel
from typing import List, Optional
from fastapi import File, UploadFile

class PushNotification(BaseModel):
    title: str
    body: str
    
    def __str__(self):
        return f"Title: {self.title}\nBody: {self.body}"
    
    def dict(self):
        return {"title": self.title, "body": self.body}
    
class PushRequest(BaseModel):
    push_type: str
    cast_name: str
    series_name: str
    creativity: int = 0.2
    demographics: List[int] = [0, 100]
    isEmojis: bool = True
    isSlangs: bool = True
    addRequirements: Optional[str]
    otherSupportingDocuments: Optional[List[UploadFile]]
    selected_trend: Optional[str]

class PushResponse(BaseModel):
    eng_push: PushNotification
    malay_push: PushNotification