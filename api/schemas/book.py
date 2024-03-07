from pydantic import BaseModel, Field

class BookCreateRequest(BaseModel):
    title: str = Field(..., example="モモ")
    author: str = Field(..., example="ミヒャエル・エンデ")
    date: str = Field(..., example="1973-09-01")
    ganre: str = Field(..., example="ファンタジー")
    
class BookDetailResponse(BaseModel):
    id: str
    title: str
    author: str
    date: str
    ganre: str
    
class BookListResponse(BaseModel):
    books: list[BookDetailResponse]