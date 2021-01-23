from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud_comment, schemas
from database.conn import get_db 

# 프론트와 상호작용

# 에디터 별 코멘트
# 메뉴 별 코멘트

'''
에러 핸들링
1. editor_id, menu_id가 db에 없는 경우(해야하나?)
2. 있지만 반환되는 리스트가 비어있는 경우
'''

router = APIRouter(prefix='/comments')

@router.get("/editors/{editor_id}", response_model=List[schemas.Comment])
def comment_editor(
    editor_id: int,
    db: Session = Depends(get_db)):

    comments = crud_comment.get_comments_per_editor(db, editor_id = editor_id)

    if not comments: # 해당하는 코멘트가 없는 경우
        raise HTTPException(status_code=404)
    return comments

@router.get("/menus/{menu_id}", response_model=List[schemas.Comment])
def comment_menu(
    menu_id: int,
    db: Session = Depends(get_db)):

    comments = crud_comment.get_comments_per_menu(db, menu_id = menu_id)

    if not comments:
        raise HTTPException(status_code=404)
    return comments
