from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from bot import DB_HOST, DB_USER,DB_PASSWORD,DB_NAME


# MySQL connection string format:
DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

def start() -> scoped_session:
    
    engine=create_engine(DATABASE_URI)
    base.metadata.bind=engine
    base.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine,autoflush=False))
    
base=declarative_base()
session=start()