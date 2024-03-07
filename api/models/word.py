from sqlalchemy import Column, String, DateTime, func
from api.db import Base, generate_uuid

class Word(Base):
    __tablename__ = "words"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    book_id = Column(String, nullable=False)
    word = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())