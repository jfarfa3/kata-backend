from sqlalchemy import Column, Integer, String, DateTime, Enum as SqlEnum, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.domain.enums import MovieFormat
from app.domain.associations import movie_tags
from app.infraestructure.database import Base

class Movie(Base):
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  genre = Column(String, nullable=False)
  duration = Column(Integer, nullable=False)
  classification = Column(String, nullable=False)
  format = Column(SqlEnum(MovieFormat), nullable=False)
  tags = relationship('Tag', secondary=movie_tags, back_populates='movies')