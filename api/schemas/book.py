from pydantic import BaseModel, Field

class BookCreateRequest(BaseModel):
    title: str = Field(..., example="モモ")
    author: str = Field(..., example="ミヒャエル・エンデ")
    date: str = Field(..., example="1973-09-01")
    genre: str = Field(..., example="ファンタジー")
    
class BookDetailResponse(BaseModel):
    id: str
    title: str
    author: str
    date: str
    genre: str
    
class BookListResponse(BaseModel):
    books: list[BookDetailResponse]
    
class BookPutRequest(BaseModel):
    id: str = Field(..., example="1")
    title: str = Field(..., example="モモ")
    author: str = Field(..., example="ミヒャエル・エンデ")
    date: str = Field(..., example="1973-09-01")
    genre: str = Field(..., example="ファンタジー")