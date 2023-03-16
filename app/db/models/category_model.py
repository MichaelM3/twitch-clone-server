from sqlalchemy import Column, TIMESTAMP, String, Integer, text
from ..database import Base

class Category(Base):
    __tablename__ = "categories" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) 
    poster = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
