from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from .. import models

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{id}")
def show(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id: {id}")
    return user
