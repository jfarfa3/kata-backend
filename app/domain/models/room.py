from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.domain.associations import room_features
from app.infrastructure.database import Base

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    break_time = Column(Integer, nullable=False, default=15)
    features = relationship('Feature', secondary=room_features, backref='rooms')
    seats = relationship('Seat', backref='room')