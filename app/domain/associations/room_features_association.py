from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

room_features_association = Table(
  'room_features_association',
  Base.metadata,
  Column('room_id', Integer, ForeignKey('rooms.id'), primary_key=True),
  Column('feature_id', Integer, ForeignKey('features.id'), primary_key=True)
)