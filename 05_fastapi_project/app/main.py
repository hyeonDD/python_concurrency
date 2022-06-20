from ast import keyword
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
# from config import MONGO_DB_NAME,MONGO_URL

# # MongoDB
# from motor.motor_asyncio import AsyncIOMotorClient
# from odmantic import AIOEngine
from models import mongodb
from models.book import BookModel

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static") # 정적인파일 css,js.png,jpg 등 마운트용

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR/"templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬",publisher="BJpublic",price=1200,image="me.png")
    await mongodb.engine.save(book) # db 저장
    return templates.TemplateResponse(
        "./index.html",
        {"request": request,"title": "콜렉터 북북이"}
    )

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request,q: str):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request,"title": "콜렉터 북북이","keyword" : q}
    )

@app.on_event("startup")
def on_app_start():    
    mongodb.connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    mongodb.close()