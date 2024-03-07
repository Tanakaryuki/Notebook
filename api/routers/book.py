from fastapi import FastAPI, APIRouter,Depends

import api.schemas.book as book_schema
from api.db import get_db

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/books",response_model=book_schema.BookListResponse,description="Get all books",tags=["book"])
def get_books(db = Depends(get_db)):
    pass

@router.post("/book",description="Create a new book",tags=["book"])
def create_book(request: book_schema.BookCreateRequest):
    pass

@router.get("/book/{book_id}",response_model=book_schema.BookDetailResponse,description="Get a book by ID",tags=["book"])
def get_book(book_id: str, db = Depends(get_db)):
    pass

@router.delete("/book/{book_id}",description="Delete a book by ID",tags=["book"])
def delete_book(book_id: str, db = Depends(get_db)):
    pass

@router.put("/book/{book_id}",description="Update a book by ID",tags=["book"])
def update_book(book_id: str, request: book_schema.BookCreateRequest, db = Depends(get_db)):
    pass
