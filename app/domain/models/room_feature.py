from sqlalchemy import Column, Integer, String
from app.infraestructure.database import Base

class RoomFeature(Base):
    __tablename__ = 'room_features'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)