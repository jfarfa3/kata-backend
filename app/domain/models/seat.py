from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey
from app.domain.enums import SeatType
from app.infrastructure.database import Base

class Seat(Base):
    __tablename__ = 'seats'
    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    seat_type = Column(SqlEnum(SeatType), nullable=False, default=SeatType.STANDARD)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
