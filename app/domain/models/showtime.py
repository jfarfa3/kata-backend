from sqlalchemy import Column, Integer, ForeignKey, String, ARRAY, JSON
from app.infrastructure.database import Base


class Showtime(Base):
    __tablename__ = 'showtimes'
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    seats_sold = Column(ARRAY(JSON), nullable=False, default=[])

    def __str__(self):
        return f"Showtime(id={self.id}, movie_id={self.movie_id}, room_id={self.room_id}, start_time='{self.start_time}', end_time='{self.end_time}')"

    def __repr__(self):
        return self.__str__()
