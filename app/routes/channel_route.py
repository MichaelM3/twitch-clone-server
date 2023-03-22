from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..crud import crud_channel
from ..schemas import channel_schema

router = APIRouter(
    prefix="/channels",
    tags=["Channels"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[channel_schema.Channel])
def read_channels(db: Session = Depends(get_db)):
    return crud_channel.get_channels(db)
