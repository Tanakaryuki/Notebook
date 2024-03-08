from sqlalchemy import Column, String, DateTime, func
from api.db import Base, generate_uuid

class Word(Base):
    __tablename__ = "Words"
    
    id = Column(String(255), primary_key=True, default=generate_uuid)
    book_id = Column(String(255), nullable=False)
    word = Column(String(255), nullable=False)
    read = Column(String(255), nullable=False)
    page_num = Column(String(255), nullable=False)
    example = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())