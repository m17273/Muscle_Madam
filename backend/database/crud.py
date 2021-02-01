from typing import List

from sqlalchemy.orm import Session
from . import models, schemas

# menu
def get_menus_by_recommendation(
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
def get_restaurant(db: Session, restaurant_pk: int):
    return db.query(models.Restaurant).filter(models.Restaurant.restaurant_pk == restaurant_pk).first()

def get_restaurant_by_name(db: Session, restaurant_name: str):
    return db.query(models.Restaurant).filter(models.Restaurant.restaurant_name == restaurant_name).first()

def create_restaurant(db: Session, req: schemas.RestaurantRequest):
    db_rest = models.Restaurant(**req.dict())
    db.add(db_rest)
    db.commit()
    db.refresh(db_rest)

    return db_rest

def update_restaurant(db: Session, restaurant_pk: int, req: schemas.RestaurantRequest):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.restaurant_pk == restaurant_pk).first()
    req_dict = req.dict()
    req = {k: v for k,v in req_dict.items()}

    for key, value in req.items():
        setattr(db_restaurant, key, value)
    
    db.commit()
    db.refresh(db_restaurant)

    return db_restaurant

def delete_restaurant(db: Session, restaurant_pk: int):
    db_restaurant = db.query(models.Restaurant).filter(models.Restaurant.restaurant_pk == restaurant_pk).first()
    db.delete(db_restaurant)
    db.commit()

# editor
def get_editor(db: Session, editor_pk: int):
    return db.query(models.Editor).filter(models.Editor.editor_pk == editor_pk).first()

def get_editor_by_name(db: Session, editor_name: str):
    return db.query(models.Editor).filter(models.Editor.editor_name == editor_name).first()

def get_editors(db: Session):
    return db.query(models.Editor).all()

def create_editor(db: Session, req: schemas.EditorRequest):
    db_rest = models.Editor(**req.dict())
    db.add(db_rest)
    db.commit()
    db.refresh(db_rest)

    return db_rest

def update_editor(db: Session, editor_pk: int, req: schemas.EditorRequest):
    db_editor = db.query(models.Editor).filter(models.Editor.editor_pk == editor_pk).first()
    req_dict = req.dict()
    req = {k: v for k,v in req_dict.items()}

    for key, value in req.items():
        setattr(db_editor, key, value)
    
    db.commit()
    db.refresh(db_editor)

    return db_editor

def delete_editor(db: Session, editor_pk: int):
    db_editor = db.query(models.Editor).filter(models.Editor.editor_pk == editor_pk).first()
    db.delete(db_editor)
    db.commit()
