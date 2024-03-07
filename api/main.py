from fastapi import FastAPI

from dotenv import load_dotenv

load_dotenv()

from api.routers import book, word

app = FastAPI()
app.include_router(book.router, prefix="/api")
app.include_router(word.router, prefix="/api")