from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas import user_schema
from ..db.models import user_model
from ..utils import hash

def create_user(payload: user_schema.UserCreate, db: Session):
    hashed_password = hash(payload.hashed_password)
    payload.hashed_password = hashed_password
    db_user = user_model.User(**payload.dict())
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

def update_user(id: int, payload: user_schema.UserUpdate, db: Session):
    user_query = db.query(user_model.User).filter(user_model.User.id == id)
    user = user_query.first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id: {id}")

    update_data = {getattr(user_model.User, k): v for k, v in payload.dict(exclude_unset=True).items()}
    user_query.update(update_data, synchronize_session=False)

    db.commit()

    return user
