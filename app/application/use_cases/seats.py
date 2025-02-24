from sqlalchemy.orm import Session
from app.infrastructure.repositories.room_repository import save_seats_in_room
from app.infrastructure.repositories.reservation_repository import save_seats_in_reservation
from app.infrastructure.repositories.showtime_repository import save_seats_in_showtime
from app.domain.schemas.seat import SeatsCreate

def save_seats_in_room_use_case(db: Session, room_id: int, seats: SeatsCreate):
    return save_seats_in_room(db, room_id, seats)
  
def save_seats_in_reservation_use_case(db: Session, reservation_id: int, seats: SeatsCreate):
    return save_seats_in_reservation(db, reservation_id, seats)

def save_seats_in_showtime_use_case(db: Session, showtime_id: int, seats: SeatsCreate):
    return save_seats_in_showtime(db, showtime_id, seats)


