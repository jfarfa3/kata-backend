from app.domain.associations import movie_tags
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infraestructure.database import Base

class Tag(Base):
  __tablename__ = 'tags'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  movies = relationship('Movie', secondary=movie_tags, back_populates='tags')