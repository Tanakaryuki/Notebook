from sqlalchemy import Column, String,DateTime, func
from api.db import Base, generate_uuid

class Book(Base):
    __tablename__ = "Books"
    
    id = Column(String(255), primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    genre = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False,default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())