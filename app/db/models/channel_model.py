from sqlalchemy import Column, TIMESTAMP, String, Integer, Boolean, ForeignKey, text
from ..database import Base

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    is_live = Column(Boolean, default=False)
    description = Column(String, default="No bio information")
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
