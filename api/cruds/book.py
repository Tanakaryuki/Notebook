from sqlalchemy.orm import Session

import api.models.book as book_model
import api.schemas.book as book_schema

def get_books(db: Session):
    return db.query(book_model.Book).all()

def get_book_by_id(book_id: str, db: Session):
    return db.query(book_model.Book).filter(book_model.Book.id == book_id).first()

def create_book(book: book_schema.BookCreateRequest, db: Session) -> book_model.Book:
    book = book.model_dump()
    book = book_model.Book(**book)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def delete_book(book_id: str, db: Session) -> None:
    db.query(book_model.Book).filter(book_model.Book.id == book_id).delete()
    db.commit()
    return None

def update_book(book: book_schema.BookPutRequest, db: Session) -> None:
    db.query(book_model.Book).filter(book_model.Book.id == book.id).update(book.model_dump())
    db.commit()
    return None