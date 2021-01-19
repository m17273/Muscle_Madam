from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .conn import Base

class Category(Base):
    __tablename__ = "categories"

    category_pk = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(30), nullable=False)


class Kind(Base):
    __tablename__ = "kinds"

    kind_pk = Column(Integer, primary_key=True, autoincrement=True)
    kind_name = Column(String(20), nullable=False)


class Range(Base):
    __tablename__ = "ranges"

    range_pk = Column(Integer, primary_key=True, autoincrement=True)
    price_range = Column(String(30), nullable=False)


class Restaurant(Base):
    __tablename__ = "restaurants"

    restaurant_pk = Column(Integer, primary_key=True, autoincrement=True)
    retaurant_name = Column(String(20), nullable=False)
    address = Column(String(50))
    phone_number = Column(String(20))


class Editor(Base):
    __tablename__ = "editors"

    editor_pk = Column(Integer, primary_key=True, autoincrement=True)
    editor_name = Column(String(30), nullable=False)
    editor_intro = Column(String(100), nullable=False)

    comment = relationship("Comment", primaryjoin="Editor.editor_pk == Comment.editor_pk", backref="editors")


class Comment(Base):
    __tablename__ = "comments"

    comment_pk = Column(Integer, primary_key=True, autoincrement=True)
    editor_pk = Column(Integer, ForeignKey("editors.editor_pk", ondelete="CASCADE", onupdate="CASCADE"))
    menu_pk = Column(Integer, ForeignKey("menus.menu_pk", ondelete="CASCADE", onupdate="CASCADE"))
    content = Column(String(100), nullable=False)

    editor = relationship("Editor", primaryjoin="Comment.editor_pk == Editor.editor_pk", backref="comments")  


class Menu(Base):
    __tablename__ = "menus"

    menu_pk = Column(Integer, primary_key=True, autoincrement=True)
    category_pk = Column(Integer, ForeignKey("categories.category_pk", ondelete="CASCADE", onupdate="CASCADE"))
    kind_pk = Column(Integer, ForeignKey("kinds.kind_pk", ondelete="CASCADE", onupdate="CASCADE"))
    price_pk = Column(Integer, ForeignKey("ranges.range_pk", ondelete="CASCADE", onupdate="CASCADE"))
    restaurant_pk = Column(Integer, ForeignKey("restaurants.restaurant_pk", ondelete="CASCADE", onupdate="CASCADE"))
    menu_name = Column(String(20), nullable=False)
    menu_price = Column(Integer, nullable=False)
    menu_image = Column(String(100))  # 디폴트 이미지 세팅필요

    comments = relationship("Comment", primaryjoin="Menu.menu_pk == Comment.menu_pk", backref="menus")