from typing import List

from sqlalchemy.orm import Session
from . import models, schemas

def get_menus_by_select(
    db: Session,
    categories: List[int],
    kinds: List[int],
    prices: List[int]):
    return db.query(models.Menu).filter(
    models.Menu.category_pk.in_(categories), 
    models.Menu.kind_pk.in_(kinds),
    models.Menu.price_pk.in_(prices)).all()

def get_menus(db: Session):
    return db.query(models.Menu).all()

def create_menus(db: Session):
    pass

def update_menus(db: Session):
    pass

def delete_menus(db: Session):
    pass