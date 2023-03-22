from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import channel_schema
from ..db.models import channel_model

def get_channels(db: Session):
   return db.query(channel_model.Channel).all()
    
