from fastapi import FastAPI

from api.routers import book

app = FastAPI()
app.include_router(book.router, prefix="/api")