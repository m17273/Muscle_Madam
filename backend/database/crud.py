from sqlalchemy.orm import Session
from . import models, schemas

def get_menus_by_select(
    db: Session,
    category_pk: int,
    kind_pk: int,
    price_pk: int):
    return db.query(models.Menu).filter(
    models.Menu.category_pk == category_pk, 
    models.Menu.kind_pk == kind_pk,
    models.Menu.price_pk == price_pk).all()

def get_menus(db: Session):
    return db.query(models.Menu).all()
