from fastapi import FastAPI, APIRouter,Depends,HTTPException,status

import api.schemas.book as book_schema
import api.cruds.book as book_crud
from api.db import get_db

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/books",response_model=book_schema.BookListResponse,description="Get all books",tags=["book"])
def get_books(db = Depends(get_db)):
    books = book_crud.get_books(db)
    return book_schema.BookListResponse(books=books)

@router.post("/book",description="Create a new book",tags=["book"])
def create_book(request: book_schema.BookCreateRequest):
    book = book_crud.create_book(request)
    if not book:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    
    return HTTPException(status.HTTP_201_CREATED)

@router.get("/book/{book_id}",response_model=book_schema.BookDetailResponse,description="Get a book by ID",tags=["book"])
def get_book(book_id: str, db = Depends(get_db)):
    book = book_crud.get_book(book_id, db)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return book_schema.BookDetailResponse(book)

@router.delete("/book/{book_id}",description="Delete a book by ID",tags=["book"])
def delete_book(book_id: str, db = Depends(get_db)):
    book = book_crud.get_book(book_id, db)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    book_crud.delete_book(book_id, db)
    return HTTPException(status.HTTP_200_OK)

@router.put("/book/{book_id}",description="Update a book by ID",tags=["book"])
def update_book(book_id: str, request: book_schema.BookCreateRequest, db = Depends(get_db)):
    book = book_crud.get_book(book_id, db)
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    book_crud.update_book(book_id, request, db)
    return HTTPException(status.HTTP_200_OK)
