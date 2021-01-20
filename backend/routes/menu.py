from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

# 왠지 모르겠는데 상대경로가 안먹힘...
from database import crud, schemas
from database.conn import get_db 

router = APIRouter(prefix='/menus')

'''
1. params == None이면 모든 메뉴 반환
2. categories, kinds, prices가 모두 정상적으로 전달되면 200(OK)
3. 만약 하나라도 누락된다면 422에러
4. 해당되는 데이터가 없다면 404에러
'''
@router.get("/", response_model=List[schemas.Menu])
def recommend(
    categories: str = Query(None),
    kinds: str = Query(None),
    prices: str = Query(None), 
    db: Session = Depends(get_db)):

    if categories == None and kinds == None and prices == None:
        menus = crud.get_menus(db)
        return menus

    try:
        categories = list(map(int, categories.split(',')))
        kinds = list(map(int, kinds.split(',')))
        prices = list(map(int, prices.split(',')))
    except:
        raise HTTPException(status_code=422)

    menus = crud.get_menus_by_select(db, categories = categories, kinds = kinds, prices = prices)
    if menus is None:
        raise HTTPException(status_code=404)
    return menus