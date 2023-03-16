from sqlalchemy import TIMESTAMP, Column, String, Integer, Boolean, text
from ..database import Base

class User(Base):
    __tablename__ =  "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False) 
    is_creator = Column(Boolean, default=False) 
    avatar = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

