from sqlalchemy.orm import Session

import api.models.word as word_model
import api.schemas.word as word_schema

def get_words(db: Session, book_id: str):
    return db.query(word_model.Word).filter(word_model.Word.book_id == book_id).all()

def get_word_by_id(db: Session, word_id: str):
    return db.query(word_model.Word).filter(word_model.Word.id == word_id).first()

def create_word(request: word_schema.WordCreateRequest, db: Session) -> word_model.Word:
    word = word_model.Word(**request.model_dump())
    db.add(word)
    db.commit()
    db.refresh(word)
    return word

def delete_word(word_id: str, db: Session) -> None:
    db.query(word_model.Word).filter(word_model.Word.id == word_id).delete()
    db.commit()
    return None

def update_word(request: word_schema.WordPutRequest, db: Session,word_id: str) -> None:
    db.query(word_model.Word).filter(word_model.Word.id == word_id).update(request.model_dump())
    db.commit()
    return None