from sqlalchemy.orm import Session
from app.domain.models import Room
from app.domain.schemas.seat import SeatsCreate


def get_all_rooms(db: Session):
    return db.query(Room).all()


def get_room_by_id(db: Session, room_id: int):
    room = db.query(Room).filter(Room.id == room_id).first()
    return room


def create_room(db: Session, room: Room):
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def save_seats_in_room(db: Session, room_id: int, seats: SeatsCreate):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        return None
    seats_dic = [seat.dict() for seat in seats.seats]
    room.seats = seats_dic
    db.commit()
    return room


def update_room(db: Session, room_id: int, room: Room):
    try:
        db.query(Room).filter(Room.id == room_id).update(room.dict())
        db.commit()
    except Exception as e:
        raise e
    return room


def delete_room(db: Session, room_id: int):
    try:
        room = db.query(Room).filter(Room.id == room_id).first()
        if not room:
            return None
        db.delete(room)
        db.commit()
        return room

    except Exception as e:
        db.rollback()
        raise e
