from typing import List

import shutil
import os

from fastapi import APIRouter, Depends, HTTPException, Response, File, UploadFile, Form
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud, schemas
from database.conn import get_db 

router = APIRouter(prefix='/menus')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'static/')
SERVER_IMG_DIR = os.path.join('http://localhost:8080/', 'static/')

@router.post("/", response_model=schemas.Menu)
async def create_menu(
    category_pk: int = Form(...),
    kind_pk: int = Form(...),
    price_pk: int = Form(...),
    restaurant_pk: int = Form(...),
    menu_name: str = Form(...),
    menu_price: int = Form(...),
    menu_image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    db_menu = crud.get_menu_by_select(
        db,
        category_pk = category_pk,
        kind_pk = kind_pk,
        price_pk = price_pk,
        menu_name = menu_name)
    
    if db_menu: # 중복된 이름의 메뉴가 존재하면 400 반환
        raise HTTPException(status_code=400)
    
    server_path = ''
    
    if menu_image != None: # 사진이 존재한다면
        local_path = os.path.join(IMG_DIR, 'images/', menu_image.filename)
        with open(local_path, 'wb') as buffer:
            shutil.copyfileobj(menu_image.file, buffer)
        server_path = os.path.join(SERVER_IMG_DIR, 'images/', menu_image.filename)

    req = schemas.MenuRequest(
    category_pk = category_pk,
    kind_pk = kind_pk,
    price_pk = price_pk,
    restaurant_pk = restaurant_pk,
    menu_name = menu_name,
    menu_price = menu_price,
    menu_image = server_path,
    )

    menu = crud.create_menu(db, req)

    return menu


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

@router.put("/", response_model=schemas.Menu)
async def update_menu(
    menu_pk: int = Form(...),
    category_pk: int = Form(...),
    kind_pk: int = Form(...),
    price_pk: int = Form(...),
    restaurant_pk: int = Form(...),
    menu_name: str = Form(...),
    menu_price: int = Form(...),
    menu_image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    menu = crud.get_menu(db, menu_pk)

    if menu is None:
        raise HTTPException(status_code=404)
    
    server_path = ''
    
    if menu_image != None: # 사진이 존재한다면
        local_path = os.path.join(IMG_DIR, 'images/', menu_image.filename)
        with open(local_path, 'wb') as buffer:
            shutil.copyfileobj(menu_image.file, buffer)
        server_path = os.path.join(SERVER_IMG_DIR, 'images/', menu_image.filename)

    req = schemas.Menu(
    menu_pk = menu_pk,
    category_pk = category_pk,
    kind_pk = kind_pk,
    price_pk = price_pk,
    restaurant_pk = restaurant_pk,
    menu_name = menu_name,
    menu_price = menu_price,
    menu_image = server_path,
    )

    menu = crud.update_menu(db, menu_pk, req)

    return menu


@router.delete("/{menu_pk}")
def delete_menu(menu_pk: int, db: Session = Depends(get_db)):
    menu = crud.get_menu(db, menu_pk)

    if menu is None:
        raise HTTPException(status_code=404)

    crud.delete_menu(db, menu_pk)

    return Response(status_code=204) 
    