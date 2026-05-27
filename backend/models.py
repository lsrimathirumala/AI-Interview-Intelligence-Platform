from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    filename = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False)
    content_type = Column(Text)
    uploaded_at = Column(DateTime(timezone=False), server_default=func.now())