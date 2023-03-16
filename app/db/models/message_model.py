from sqlalchemy import Column, TIMESTAMP, String, Integer, ForeignKey, text
from ..database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    sender_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    stream_id = Column(Integer, ForeignKey("streams.id", ondelete="CASCADE"))

