from pydantic import BaseModel
    
class PushNotification(BaseModel):
    title: str
    body: str
    explanation: str
    
    def __str__(self):
        return f"Title: {self.title}\nBody: {self.body}"
    
    def dict(self):
        return {"title": self.title, "body": self.body}
    
class PushRequest(BaseModel):
   cast_name: str
   series_name: str
   episode_idx: int

class PushResponse(BaseModel):
    eng_push: PushNotification
    malay_push: PushNotification