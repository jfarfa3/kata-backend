from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)