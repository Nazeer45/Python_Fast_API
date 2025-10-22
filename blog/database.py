from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# check_same_thread = False is required for sqlite database to work with FastAPI in a multi-threaded environment

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#sessionmaker is a function that generates database sessions
#autocommit=False means that the database will not commit the changes to the database automatically
#autoflush=False means Prevents automatic flushing of objects to the database
#bind=engine means that the session will use the engine to connect to the database

Base = declarative_base()
# Base class for all database models, every model inherits from it

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()