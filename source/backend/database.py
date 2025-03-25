from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autoflush = False, autocommit = False, bind=engine)

Base = sessionlocal()

def get_db():
    try:
        db = sessionlocal()
    finally:
        db.close()