from fastapi import HTTPException, status
from sqlalchemy.orm import Session
# from ..schemas import channel_schema
from ..db.models import channel_model

def get_channels(db: Session):
    return db.query(channel_model.Channel).all()
    
def get_channel(id: int, db: Session):
    channel = db.query(channel_model.Channel).filter(channel_model.Channel.id == id).first()

    if not channel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No channel found with id of {id}")

    return channel
