from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.models import user_model
from ..db.database import get_db
from ..schemas import auth_schema, user_schema
from ..utils import verify

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", response_model=user_schema.User)
def login(payload: auth_schema.Login, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.username == payload.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    return user
