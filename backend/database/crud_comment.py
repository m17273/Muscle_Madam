from sqlalchemy.orm import Session
from . import models, schemas

# DB와 상호작용

def get_comments_per_editor(
    db: Session,
    editor_id: int):
    return db.query(models.Comment).filter(
        models.Comment.editor_pk == editor_id)

def get_comments_per_menu(
    db: Session,
    menu_id: int):
    return db.query(models.Comment).filter(
        models.Comment.menu_pk == menu_id)

# def create_comment(
#     db: Session,
#     editor_id: int,
#     menu_id: int,
#     content: str):

# def update_comment(db: Session)

# def delete_comment(db: Session)