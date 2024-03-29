from pydantic import BaseModel, Field

class WordCreateRequest(BaseModel):
    book_id: str = Field(..., example="1")
    word: str = Field(..., example="デプロイ")
    read: str = Field(..., example="でぷろい")
    page_num: str = Field(..., example="011")
    example: str = Field(..., example="Webアプリケーションなどのシステム開発工程で、アプリケーションの機能やサービスをサーバー上に配置・展開し、利用可能な状態にする一連の作業を指す。")
    
class WordDetailResponse(BaseModel):
    id: str
    book_id: str
    word: str
    read: str
    page_num: str
    example: str
    
class WordListResponse(BaseModel):
    words: list[WordDetailResponse]
    
class WordPutRequest(BaseModel):
    word: str = Field(..., example="デプロイ")
    read: str = Field(..., example="でぷろい")
    page_num: str = Field(..., example="011")
    example: str = Field(..., example="Webアプリケーションなどのシステム開発工程で、アプリケーションの機能やサービスをサーバー上に配置・展開し、利用可能な状態にする一連の作業を指す。")