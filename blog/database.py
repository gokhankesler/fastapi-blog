from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base


BASE_URL = 'postgresql+psycopg2://postgres:password@localhost:1234/postgres'

engine = create_engine(BASE_URL)
SessionLocal = Session(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
