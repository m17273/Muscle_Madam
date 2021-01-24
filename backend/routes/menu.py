from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud, schemas
from database.conn import get_db 

router = APIRouter(prefix='/menus')

@router.post("/", response_model=schemas.Menu)
def create_menu(req: schemas.MenuRequest, db: Session = Depends(get_db)):
    db_menu = crud.get_menu_by_select(
        db,
        category_pk = req.category_pk,
        kind_pk = req.kind_pk,
        price_pk = req.price_pk,
        menu_name = req.menu_name)
    
    if db_menu:
        raise HTTPException(status_code=400)

    menu = crud.create_menu(db, req)

    return menu

'''
1. params == None이면 모든 메뉴 반환
2. categories, kinds, prices가 모두 정상적으로 전달되면 200(OK)
3. 만약 하나라도 누락된다면 400에러
4. 해당되는 데이터가 없다면 404에러
'''
@router.get("/", response_model=List[schemas.Menu])
def get_menus(
    categories: List[int] = Query(None),
    kinds: List[int] = Query(None),
    prices: List[int] = Query(None), 
    db: Session = Depends(get_db)):
    
    if categories == None and kinds == None and prices == None:
        menus = crud.get_menus(db)
        return menus

    if not categories or not kinds or not prices:
        raise HTTPException(status_code=400)

    menus = crud.get_menus_by_recommendation(db, categories, kinds, prices)

    if menus is None:
        raise HTTPException(status_code=404)
    return menus

@router.put("/{menu_pk}", response_model=schemas.Menu)
def update_menu(menu_pk: int, req: schemas.MenuRequest, db: Session = Depends(get_db)):
    menu = crud.get_menu(db, menu_pk)

    if menu is None:
        raise HTTPException(status_code=404)
    
    menu = crud.update_menu(db, menu_pk, req)

    return menu


@router.delete("/{menu_pk}")
def delete_menu(menu_pk: int, db: Session = Depends(get_db)):
    menu = crud.get_menu(db, menu_pk)

    if menu is None:
        raise HTTPException(status_code=404)

    crud.delete_menu(db, menu_pk)

    return Response(status_code=204) 
    