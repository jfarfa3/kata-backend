from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.domain.models import Base
from app.domain.associations import room_features_association
from app.infraestructure.database import Base

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    break_time = Column(Integer, nullable=False, default=15)
    features = relationship('RoomFeature', secondary=room_features_association, backref='rooms')
    seats = relationship('Seat', backref='room')