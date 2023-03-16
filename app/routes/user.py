from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..crud import crud_user
from ..schemas import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=schemas.User)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(payload, db)

@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/{id}", response_model=schemas.User)
def read_user(id: int, db: Session = Depends(get_db)):
    return crud_user.get_user(id, db)

