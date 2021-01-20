from typing import List

from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from database.conn import engine
from database import models
from routes import menu

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="muscle_madam")

# 라우터 정의
app.include_router(menu.router, tags=["Menus"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
