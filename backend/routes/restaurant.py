from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud, schemas
from database.conn import get_db 

router = APIRouter(prefix='/restaurants')

@router.post("/")
def create_restaurant(req: schemas.RestaurantRequest, db: Session = Depends(get_db)):
    db_rest = crud.get_restaurant_by_name(db, restaurant_name = req.restaurant_name)

    if db_rest:
        raise HTTPException(status_code=400)

    rest = crud.create_restaurant(db, req)

    return rest

@router.get("/{restaurant_pk}", response_model=schemas.Restaurant)
def get_restaurant(restaurant_pk: int, db: Session = Depends(get_db)):
    rest = crud.get_restaurant(db, restaurant_pk)

    if rest is None:
        raise HTTPException(status_code=404)
    
    return rest


@router.put("/{restaurant_pk}", response_model=schemas.Restaurant)
def update_restaurant(restaurant_pk: int, req: schemas.RestaurantRequest, db: Session = Depends(get_db)):
    rest = crud.get_restaurant(db, restaurant_pk)

    if rest is None:
        raise HTTPException(status_code=404)
    
    rest = crud.update_restaurant(db, restaurant_pk, req)

    return rest

@router.delete("/{restaurant_pk}")
def delete_restaurant(restaurant_pk: int, db: Session = Depends(get_db)):
    rest = crud.get_restaurant(db, restaurant_pk)

    if rest is None:
        raise HTTPException(status_code=404)

    crud.delete_restaurant(db, restaurant_pk)

    return Response(status_code=204)