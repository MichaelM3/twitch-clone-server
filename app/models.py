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
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    sent_messages = relationship("Message", back_populates="sender")
    channel = relationship("Channel", back_populates="owner", lazy="dynamic", cascade="all, delete")
    follows = relationship("Follower", back_populates="user")

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    is_live = Column(Boolean, default=False)
    description = Column(String, default="No bio information")
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner  = relationship("User", back_populates="channel", lazy="dynamic")
    followers = relationship("Follow", back_populates="channel", cascade="all, delete")
    streams = relationship("Stream", back_populates="channel", cascade="all, delete")

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    channel_id = Column(Integer, ForeignKey("channels.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="follows")
    channel = relationship("Channel", back_populates="followers")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    stream_id = Column(Integer, ForeignKey("streams.id", ondelete="CASCADE"))

    sender = relationship("User", back_populates="sent_messages")
    stream = relationship("Stream", back_populates="messages")

class Stream(Base):
    __tablename__ = "streams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    stream_key = Column(String, nullable=False)
    view_count = Column(Integer, default=0)
    thumbnail_url = Column(String, nullable=True)
    channel_id = Column(Integer, ForeignKey("channels.id", ondelete="CASCADE"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    channel = relationship("Channel", back_populates="streams")
    category = relationship("Category", back_populates="streams")
    messages = relationship("Message", back_populates="stream", cascade="all, delete")

class Category(Base):
    __tablename__ = "categories" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) 
    poster = Column(String, nullable=True)
