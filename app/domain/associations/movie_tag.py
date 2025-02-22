from sqlalchemy import Table, Column, Integer, ForeignKey
from app.infrastructure.database import Base

movie_tags = Table(
  'movie_tags_association',
  Base.metadata,
  Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
  Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)