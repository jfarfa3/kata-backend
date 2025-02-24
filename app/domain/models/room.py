from sqlalchemy import Column, Integer, String, ARRAY, JSON
from app.infrastructure.database import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    break_time = Column(Integer, nullable=False, default=15)
    seats = Column(ARRAY(JSON), nullable=False, default=[])

    def __str__(self):
        return f"Room(id={self.id}, name='{self.name}', capacity={self.capacity}, break_time={self.break_time})"

    def __repr__(self):
        return self.__str__()
