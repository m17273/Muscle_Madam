from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud_comment, schemas
from database.conn import get_db 

# 프론트와 상호작용

# GET 에디터 별 코멘트
# GET 메뉴 별 코멘트

# POST / 바로 보내기
# DELETE /{comment_pk} 하나 삭제
# UPDATE /{comment_pk} 하나 업데이트

router = APIRouter(prefix='/comments')

@router.get("/editors/{editor_id}", response_model=List[schemas.Comment])
def comment_editor(editor_id: int, db: Session = Depends(get_db)):
    comments = crud_comment.get_comments_per_editor(db, editor_id)
    return comments

@router.get("/menus/{menu_id}", response_model=List[schemas.Comment])
def comment_menu(menu_id: int, db: Session = Depends(get_db)):
    comments = crud_comment.get_comments_per_menu(db, menu_id)
    return comments

@router.post("/", response_model=schemas.Comment, status_code=201)
def create_comment(req: schemas.CommentRequest, db: Session = Depends(get_db)):
    comment = crud_comment.get_comment_of_specific_menu_editor(
        db, menu_id = req.menu_pk, editor_id = req.editor_pk)
    # 만약 해당 메뉴에 해당 에디터가 쓴 코멘트가 있다면 에러
    if comment:
        raise HTTPException(status_code=409)

    comment = crud_comment.create_menu(db, req)
    return comment

@router.put("/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, req: schemas.CommentRequest, db: Session = Depends(get_db)):
    # 해당하는 코멘트가 존재하는지 확인
    comment = crud_comment.get_comment_by_id(db, comment_id)
    return crud_comment.update_comment(db, comment_id, req)

@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = crud_comment.get_comment_by_id(db, comment_id)
    return crud_comment.delete_comment(db, comment_id)