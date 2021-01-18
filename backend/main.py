import sys
from fastapi import FastAPI
import uvicorn

from sqlalchemy.orm import Session, sessionmaker

import sqlalchemy.orm.session

import models
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="muscle_madam")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)