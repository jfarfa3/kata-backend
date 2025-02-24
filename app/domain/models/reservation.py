from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey, ARRAY, JSON
from app.infrastructure.database import Base
from app.domain.enums import ReservationState


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, index=True)
    user_phone = Column(String, nullable=False)
    state = Column(SqlEnum(ReservationState),
                   default=ReservationState.PENDING, index=True)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seats = Column(ARRAY(JSON), nullable=False, default=[])

    def __str__(self):
        return f"Reservation(id={self.id}, user_name='{self.user_name}', user_email='{self.user_email}', user_phone='{self.user_phone}', state='{self.state}', showtime_id={self.showtime_id})"

    def __repr__(self):
        return self.__str__()
