from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user_schema
from ..db.models import user_model
from ..hashing import Hash

def create_user(payload: user_schema.UserCreate, db: Session):
    hashed_password = Hash.bcrypt(payload.plain_password)
    db_user = models.User(username=payload.username, hashed_password=hashed_password, email=payload.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(user_model.User).all()

def get_user(id: int, db: Session):
    user = db.query(user_model.User).filter(user_model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id: {id}")
    return user

