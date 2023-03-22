from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..crud import crud_user
from ..schemas import user_schema

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.User)
def create_user(payload: user_schema.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(payload, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[user_schema.User])
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=user_schema.User)
def read_user(id: int, db: Session = Depends(get_db)):
    return crud_user.get_user(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=user_schema.User)
def update_user(id: int, payload: user_schema.UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(id, payload, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(id: int, db: Session = Depends(get_db)):
    return crud_user.destroy_user(id, db)
