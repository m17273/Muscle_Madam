from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud_comment, schemas
from database.conn import get_db 

# 프론트와 상호작용

# 에디터 별 코멘트
# 메뉴 별 코멘트

router = APIRouter(prefix='/comments')

@router.get("/editors/{editor_id}", response_model=List[schemas.Comment])
def comment_editor(
    editor_id: int,
    db: Session = Depends(get_db)):

    comments = crud_comment.get_comments_per_editor(db, editor_id = editor_id)

    if comments is None:
        raise HTTPException(status_code=404)
    print(comments)
    return comments

@router.get("/menus/{menu_id}", response_model=List[schemas.Comment])
def comment_menu(
    menu_id: int,
    db: Session = Depends(get_db)):
    print("*********************")
    print(menu_id)

    comments = crud_comment.get_comments_per_menu(db, menu_id = menu_id)
    print(comments)
    if comments is None:
        raise HTTPException(status_code=404)
    
    return comments