from typing import List

from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from sqlalchemy.orm import Session, sessionmaker
from database.conn import SessionLocal, engine
from database import models
from routes import menu

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="muscle_madam")

### for test ###

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(menu.router, tags=["Menus"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
