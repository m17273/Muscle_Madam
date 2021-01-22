from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.param_functions import Query
from sqlalchemy.orm import Session

from database import crud, schemas
from database.conn import get_db 