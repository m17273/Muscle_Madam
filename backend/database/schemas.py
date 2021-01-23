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

class RestaurantRequest(BaseModel):
    restaurant_name: str
    address: Optional[str] = None
    phone_number: Optional[str] = None

class Restaurant(BaseModel):
    restaurant_pk: int
    restaurant_name: str
    address: Optional[str] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True

class CommentRequest(BaseModel):
    editor_pk: int
    menu_pk: int
    content: str

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
    comments: Optional[List[Comment]] = []

    class Config:
        orm_mode = True

class MenuRequest(BaseModel):
    category_pk: int
    kind_pk: int
    price_pk: int
    restaurant_pk: int
    menu_name: str
    menu_price: int
    menu_image: Optional[str] = None

class Menu(BaseModel):
    menu_pk: int
    category_pk: int
    kind_pk: int
    price_pk: int
    restaurant_pk: int
    menu_name: str
    menu_price: int
    menu_image: Optional[str] = None
    comments: Optional[List[Comment]] = []

    class Config:
        orm_mode = True