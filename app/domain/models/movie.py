from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from app.domain.enums import MovieFormat
from app.infrastructure.database import Base

class Movie(Base):
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  genre = Column(String, nullable=False)
  duration = Column(Integer, nullable=False)
  classification = Column(String, nullable=False)
  format = Column(SqlEnum(MovieFormat), nullable=False)

  def __str__(self):
    return f"Movie(id={self.id}, title='{self.title}', genre='{self.genre}', duration={self.duration}, classification='{self.classification}', format='{self.format}')"

  def __repr__(self):
      return self.__str__()