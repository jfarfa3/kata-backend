from sqlalchemy.orm import Session
from app.domain.models.seat import Seat

def get_all_seats_by_room_id(db: Session, room_id: int):
    return db.query(Seat).filter(Seat.room_id == room_id).all()

def create_seat(db: Session, seat: Seat):
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat

def update_seat(db: Session, seat: Seat):
    db.query(Seat).filter(Seat.id == seat.id).update(seat)
    db.commit()
    db.refresh(seat)
    return seat

def delete_seat(db: Session, seat: Seat):
    db.delete(seat)
    db.commit()
    return seat