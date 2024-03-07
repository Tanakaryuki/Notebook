from sqlalchemy import Column, String,Datetime, func
from api.db import Base, generate_uuid

class Book(Base):
    __tablename__ = "books"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    created_at = Column(Datetime, nullable=False,default=func.now())
    updated_at = Column(Datetime, onupdate=func.now())