from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, models
from .hashing import Hash

def create_user(payload: schemas.UserCreate, db: Session):
    hashed_password = Hash.bcrypt(payload.plain_password)
    db_user = models.User(username=payload.username, hashed_password=hashed_password, email=payload.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id: {id}")
    return user

