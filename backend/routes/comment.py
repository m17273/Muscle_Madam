from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud_comment, schemas
from database.conn import get_db 

# 프론트와 상호작용

# 에디터 별 코멘트
# 메뉴 별 코멘트

router = APIRouter(prefix='/comments')

@router.get("/editors", response_model=schemas.Comment)
def comment(
    editor_id: str = Query(None),
    db: Session = Depends(get_db)):

    comments = crud_comment.get_comments_per_editor(db, editor_id = int(editor_id))

    if comments is None:
        raise HTTPException(status_code=404)
    
    return comments

@router.get("/menus", response_model=schemas.Comment)
def comment(
    menu_id: str = Query(None),
    db: Session = Depends(get_db)):

    comments = crud_comment.get_comments_per_menu(db, menu_id = int(editor_id))
    
    if comments is None:
        raise HTTPException(status_code=404)
    
    return comments