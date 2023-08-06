import os

from typing import List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
import uvicorn

from database.conn import engine
from database import models
from routes import menu, restaurant, comment, editor

from starlette.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'static', 'images')

app = FastAPI(title="muscle_madam")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 정의
app.include_router(menu.router, tags=["Menus"])
app.include_router(comment.router, tags=["Comments"])
app.include_router(restaurant.router, tags=["Restaurants"])
app.include_router(editor.router, tags=["Editors"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

# 사진 
@app.get("/static/images/{filename}")
async def main(filename:str):
    return FileResponse(f"{IMG_DIR}\{filename}")