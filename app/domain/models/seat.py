from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.domain.enums import SeatType
from app.infrastructure.database import Base
from app.domain.associations import reservation_seats

class Seat(Base):
    __tablename__ = 'seats'
    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    seat_type = Column(SqlEnum(SeatType), nullable=False, default=SeatType.STANDARD)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=True)
    reservations = relationship("Reservation", secondary=reservation_seats, back_populates="seats")
