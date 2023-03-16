from sqlalchemy import Column, TIMESTAMP, String, Integer, ForeignKey, text
from ..database import Base

class Stream(Base):
    __tablename__ = "streams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    ended_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    stream_key = Column(String, nullable=False)
    view_count = Column(Integer, default=0)
    thumbnail_url = Column(String, nullable=True)
    channel_id = Column(Integer, ForeignKey("channels.id", ondelete="CASCADE"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
