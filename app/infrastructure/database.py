from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost:5436/cinema')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def init_db():
  import app.domain.models.movie
  import app.domain.models.room
  import app.domain.models.showtime
  import app.domain.models.reservation

  Base.metadata.create_all(bind=engine)
