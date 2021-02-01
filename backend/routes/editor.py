from typing import List

import shutil
import os

from fastapi import APIRouter, Depends, HTTPException, Response, File, UploadFile, Form
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud, schemas
from database.conn import get_db 

router = APIRouter(prefix='/editors')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'static/')
SERVER_IMG_DIR = os.path.join('http://localhost:8080/', 'static/')

@router.post("/", response_model=schemas.Editor)
async def create_editor(
    editor_name: str = Form(...),
    editor_intro: str = Form(...),
    editor_image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    db_editor = crud.get_editor_by_name(db, editor_name = editor_name) 
    
    if db_editor: # 중복된 이름의 에디터가 존재하면 400 반환
        raise HTTPException(status_code=400)
    
    server_path = ''
    
    if editor_image != None: # 사진이 존재한다면
        local_path = os.path.join(IMG_DIR, 'images/', editor_image.filename)
        with open(local_path, 'wb') as buffer:
            shutil.copyfileobj(editor_image.file, buffer)
        server_path = os.path.join(SERVER_IMG_DIR, 'images/', editor_image.filename)

    req = schemas.EditorRequest(
    editor_name = editor_name,
    editor_intro = editor_intro,
    editor_image = server_path
    )

    editor = crud.create_editor(db, req)

    return editor


@router.get("/", response_model=List[schemas.Editor])
def get_editor(editor_pk: int = Query(None), db: Session = Depends(get_db)):
    if editor_pk == None: # editor_pk가 없다면 전체 editor 가져옴
        editors = crud.get_editors(db)
        return editors

    editor = crud.get_editor(db, editor_pk)

    if editor is None:
        raise HTTPException(status_code=404)
    
    return editor

@router.put("/", response_model=schemas.Editor)
async def update_editor(
    editor_pk: int = Form(...),
    editor_name: str = Form(...),
    editor_intro: str = Form(...),
    editor_image: UploadFile = File(None),
    db: Session = Depends(get_db)):

    editor = crud.get_editor(db, editor_pk)

    if editor is None:
        raise HTTPException(status_code=404)
    
    server_path = ''
    
    if editor_image != None: # 사진이 존재한다면
        local_path = os.path.join(IMG_DIR, 'images/', editor_image.filename)
        with open(local_path, 'wb') as buffer:
            shutil.copyfileobj(editor_image.file, buffer)
        server_path = os.path.join(SERVER_IMG_DIR, 'images/', editor_image.filename)

    req = schemas.EditorRequest(
    editor_name = editor_name,
    editor_intro = editor_intro,
    editor_image = server_path
    )

    editor = crud.update_editor(db, editor_pk, req)

    return editor


@router.delete("/{editor_pk}")
def delete_editor(editor_pk: int, db: Session = Depends(get_db)):
    editor = crud.get_editor(db, editor_pk)

    if editor is None:
        raise HTTPException(status_code=404)

    crud.delete_editor(db, editor_pk)

    return Response(status_code=204) 
    