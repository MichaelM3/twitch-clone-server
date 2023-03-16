from sqlalchemy.orm import relationship
from .user_model import User
from .message_model import Message
from .channel_model import Channel
from .stream_model import Stream
from .follow_model import Follow
from .category_model import Category

User.sent_messages = relationship("Message", back_populates="sender")
User.channel = relationship("Channel", back_populates="owner", cascade="all, delete")
User.follows = relationship("Follow", back_populates="user")

Message.sender = relationship("User", back_populates="sent_messages")
Message.stream = relationship("Stream", back_populates="messages")

Channel.owner  = relationship("User", back_populates="channel")
Channel.followers = relationship("Follow", back_populates="channel", cascade="all, delete")
Channel.streams = relationship("Stream", back_populates="channel", cascade="all, delete")

Follow.user = relationship("User", back_populates="follows")
Follow.channel = relationship("Channel", back_populates="followers")

Stream.channel = relationship("Channel", back_populates="streams")
Stream.category = relationship("Category", back_populates="streams")
Stream.messages = relationship("Message", back_populates="stream", cascade="all, delete")

Category.streams = relationship("Stream", back_populates="category")
