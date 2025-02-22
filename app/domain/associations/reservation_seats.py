from sqlalchemy import Column, Integer, Table, ForeignKey
from app.infrastructure.database import Base

reservation_seats = Table(
    'reservation_seats_association',
    Base.metadata,
    Column('reservation_id', Integer, ForeignKey('reservations.id'), primary_key=True),
    Column('seat_id', Integer, ForeignKey('seats.id'), primary_key=True)
)
