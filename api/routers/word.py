from fastapi import FastAPI, APIRouter, Depends,HTTPException,status

import api.schemas.word as word_schema
import api.cruds.word as word_crud

from api.db import get_db

router = APIRouter()

@router.get("/words/{book_id}", response_model=word_schema.WordListResponse, description="Get all words", tags=["word"])
def get_words(book_id: str,db=Depends(get_db)):
    words = word_crud.get_words(db, book_id)
    word_details = [word_schema.WordDetailResponse(
        id=word.id,
        book_id=word.book_id,
        word=word.word,
        read=word.read,
        example=word.example,
        page_num=word.page_num
    ) for word in words]
    return word_schema.WordListResponse(words=word_details)

@router.post("/word", description="Create a new word", tags=["word"])
def create_word(request: word_schema.WordCreateRequest,db=Depends(get_db)):
    word = word_crud.create_word(db=db, request=request)
    if not word:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    
    return status.HTTP_201_CREATED

@router.delete("/word/{word_id}", description="Delete a word by ID", tags=["word"])
def delete_word(word_id: str, db=Depends(get_db)):
    word = word_crud.get_word_by_id(db=db, word_id=word_id)
    if not word:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    word_crud.delete_word(word_id, db)
    return status.HTTP_200_OK

@router.put("/word/{word_id}", description="Update a word by ID", tags=["word"])
def update_word(word_id: str, request: word_schema.WordPutRequest, db=Depends(get_db)):
    word = word_crud.get_word_by_id(db=db, word_id=word_id)
    if not word:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    word_crud.update_word(db=db, request=request, word_id=word_id)
    return status.HTTP_200_OK
