from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

# DB와 상호작용

def get_comments_per_editor(db: Session, editor_id: int):
    comments = db.query(models.Comment).filter(
        models.Comment.editor_pk == editor_id).all()
    if not comments: # 해당하는 코멘트가 없는 경우
        raise HTTPException(status_code=404)
    return comments

def get_comments_per_menu(db: Session, menu_id: int):
    comments = db.query(models.Comment).filter(models.Comment.menu_pk == menu_id).all()
    if not comments:
        raise HTTPException(status_code=404)
    return comments

def get_comment_of_specific_menu_editor(db: Session, menu_id: int, editor_id: int):
    return db.query(models.Comment).filter(
        models.Comment.menu_pk == menu_id,
        models.Comment.editor_pk == editor_id
    ).first()

def get_comment_by_id(db: Session, comment_id: int):
    comment = db.query(models.Comment).filter(
        models.Comment.comment_pk == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404)
    return comment

def create_menu(db: Session, req: schemas.CommentRequest):
    db_comment = models.Comment(**req.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, req: schemas.CommentRequest):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_pk == comment_id).first()
    req_dict = req.dict()
    
    for key in req_dict:
        setattr(db_comment, key, req_dict[key])

    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_pk == comment_id).first()
    db.delete(db_comment)
    db.commit()
    return