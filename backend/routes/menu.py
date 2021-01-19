from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models, crud, schemas
from database import get_db

router = APIRouter(prefix='/menus')

# 전체 메뉴
@router.get("/", response_model=List[schemas.Menu])
def all(db: Session = Depends(get_db)):
    menus = crud.get_menus(db)
    return menus

# 추천에 의한 메뉴(카테고리, 종류, 가격대)
@router.get("/{category_pk}/{kind_pk}/{price_pk}", response_model=List[schemas.Menu])
def recommend(category_pk: int, kind_pk:int, price_pk:int, db: Session = Depends(get_db)):
    menus = crud.get_menus_by_select(db, category_pk=category_pk, kind_pk=kind_pk, price_pk=price_pk)
    if menus is None:
        raise HTTPException(status_code=404)
    return menus
