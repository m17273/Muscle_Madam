from typing import List

from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from sqlalchemy.orm import Session, sessionmaker
import models, crud, schemas
from database import SessionLocal, engine

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

# 전체 메뉴
@app.get("/menus/", response_model=List[schemas.Menu])
def all(db: Session = Depends(get_db)):
    menus = crud.get_menus(db)
    return menus

# 추천에 의한 메뉴(카테고리, 종류, 가격대)
@app.get("/menus/{category_pk}/{kind_pk}/{price_pk}", response_model=List[schemas.Menu])
def recommend(category_pk: int, kind_pk:int, price_pk:int, db: Session = Depends(get_db)):
    menus = crud.get_menus_by_select(db, category_pk=category_pk, kind_pk=kind_pk, price_pk=price_pk)
    menus = list(menus)
    if menus is None:
        raise HTTPException(status_code=404)
    return menus    


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
