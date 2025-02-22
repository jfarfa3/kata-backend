from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infraestructure.database import Base
from app.domain.associations import reservation_seats

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_email = Column(String, index=True)
    user_phone = Column(String, index=True)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seats = relationship('Seat', secondary=reservation_seats, back_populates='reservations')