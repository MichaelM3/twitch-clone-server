from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..crud import crud_user
from ..schemas import user_schema

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=user_schema.User)
def create_user(payload: user_schema.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(payload, db)

@router.get("/", response_model=List[user_schema.User])
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/{id}", response_model=user_schema.User)
def read_user(id: int, db: Session = Depends(get_db)):
    return crud_user.get_user(id, db)

@router.put("/{id}", response_model=user_schema.User)
def update_user(id: int, payload: user_schema.UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(id, payload, db)

@router.delete("/{id}")
def destroy_user(id: int, db: Session = Depends(get_db)):
    return crud_user.destroy_user(id, db)
