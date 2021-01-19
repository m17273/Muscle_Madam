from backend.models import Category
from typing import List, Optional

from pydantic import BaseModel

class Category(BaseModel):
    category_pk: int
    category_name: str

class Kind(BaseModel):
    kind_pk: int
    kind_name: str

class Range(BaseModel):
    range_pk: int
    price_range: str

class Restaurant(BaseModel):
    restaurant_pk: int
    address: Optional[str] = None
    phone_number: Optional[str] = None

class Menu(BaseModel):
    menu_pk: int
    category_pk: int
    kind_pk: int
    price_pk: int
    restaurant_pk: int
    menu_name: str
    menu_price: int
    menu_image: Optional[str] = None

    class Config:
        orm_mode = True

class Comment(BaseModel):
    comment_pk: int
    editor_pk: int
    menu_pk: int
    content: str

    class Config:
        orm_mode = True

class Editor(BaseModel):
    editor_pk: int
    editor_name: str
    editor_intro: str
    comments: List[Comment] = []

    class Config:
        orm_mode = True

