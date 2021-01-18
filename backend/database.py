import os, json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import sqlalchemy as db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_engine(
    DB_URL, encoding = 'utf-8'
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

# connection = engine.connect()
# metadata = db.MetaData()
# table = db.Table('menus', metadata, autoload=True, autoload_with=engine)

# print(table.columns.keys())