from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ =  "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False) 
    is_creator = Column(Boolean, default=False) 
    avatar = Column(String, nullable=True)

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    is_live = Column(Boolean, default=False)
    description = Column(String, default="No bio information")
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner  = relationship("User", back_populates="channels")
    followers = relationship("Follow", back_populates="channel")

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    channel_id = Column(Integer, ForeignKey("channels.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="follows")
    channel = relationship("Channel", back_populates="followers")
