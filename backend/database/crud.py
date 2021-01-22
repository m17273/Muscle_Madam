from typing import List

from sqlalchemy.orm import Session
from . import models, schemas

# about menu #
# menu
def get_menus_by_recommend(
    db: Session,
    categories: List[int],
    kinds: List[int],
    prices: List[int]):

    return db.query(models.Menu).filter(
    models.Menu.category_pk.in_(categories), 
    models.Menu.kind_pk.in_(kinds),
    models.Menu.price_pk.in_(prices)).all()

def get_menu_by_select(
    db: Session,
    category_pk: int,
    kind_pk: int,
    price_pk: int,
    menu_name: str):

    return db.query(models.Menu).filter(
    models.Menu.category_pk == category_pk, 
    models.Menu.kind_pk == kind_pk,
    models.Menu.price_pk == price_pk,
    models.Menu.menu_name == menu_name
    ).first()


def get_menus(db: Session):
    return db.query(models.Menu).all()


def get_menu(db: Session, menu_pk: int):
    return db.query(models.Menu).filter(models.Menu.menu_pk == menu_pk).first()


def create_menu(db: Session, req: schemas.MenuRequest):
    db_menu = models.Menu(**req.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    return db_menu


def update_menu(db: Session, menu_pk: int, req: schemas.MenuRequest):
    db_menu = db.query(models.Menu).filter(models.Menu.menu_pk == menu_pk).first()
    req_dict = req.dict()
    req = {k: v for k,v in req_dict.items()}

    for key, value in req.items():
        setattr(db_menu, key, value)
    
    db.commit()
    db.refresh(db_menu)

    return db_menu


def delete_menu(db: Session, menu_pk: int):
    db_menu = db.query(models.Menu).filter(models.Menu.menu_pk == menu_pk).first()
    db.delete(db_menu)
    db.commit()


# restaurant
def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()

def get_restaurant(restaurant_pk: int, db: Session):
    return db.query(models.Restaurant).filter(models.Restaurant.restaurant_pk == restaurant_pk).first()

def create_restaurant(db: Session):
    return

def update_restaurant(db: Session):
    return

def delete_restaurant(db: Session):
    return
# about menu #