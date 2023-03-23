from pydantic import BaseModel
from datetime import datetime

class ChannelBase(BaseModel):
    description: str

class ChannelCreate(ChannelBase):
    pass   

class Channel(ChannelBase):
    id: int
    owner_id: int
    is_live: bool
    created_at: datetime

    class Config:
        orm_mode = True
