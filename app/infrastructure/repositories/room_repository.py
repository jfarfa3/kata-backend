from sqlalchemy.orm import Session
from app.domain.models import Room

def get_all_rooms(db: Session):
    return db.query(Room).all()

def get_room_by_id(db: Session, room_id: int):
    return db.query(Room).filter(Room.id == room_id).first()

def create_room(db: Session, room: Room):
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def update_room(db: Session, room: Room):
    db.query(Room).filter(Room.id == room.id).update(room)
    db.commit()
    db.refresh(room)
    return room

def update_room_break_time(db: Session, room: Room, break_time: int):
    db.query(Room).filter(Room.id == room.id).update({'break_time': break_time})
    db.commit()
    db.refresh(room)
    return room

def delete_room(db: Session, room: Room):
    db.delete(room)
    db.commit()
    return room