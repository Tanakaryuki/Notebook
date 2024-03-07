from fastapi import FastAPI, APIRouter, Depends

import api.schemas.word as word_schema

from api.db import get_db

router = APIRouter()

@router.get("/words/{book_id}", response_model=word_schema.WordListResponse, description="Get all words", tags=["word"])
def get_words(book_id: str,db=Depends(get_db)):
    pass

@router.post("/word", description="Create a new word", tags=["word"])
def create_word(request: word_schema.WordCreateRequest):
    pass

@router.delete("/word/{word_id}", description="Delete a word by ID", tags=["word"])
def delete_word(word_id: str, db=Depends(get_db)):
    pass

@router.put("/word/{word_id}", description="Update a word by ID", tags=["word"])
def update_word(word_id: str, request: word_schema.WordPutRequest, db=Depends(get_db)):
    pass
