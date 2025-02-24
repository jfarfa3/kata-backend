from sqlalchemy.orm import Session
from app.infrastructure.repositories.room_repository import get_all_rooms, get_room_by_id, update_room, delete_room, create_room
from app.domain.models.room import Room
from app.domain.schemas.room import RoomUpdate, RoomCreate

def create_room_use_case(db: Session, room_data: RoomCreate):
    room = Room(**room_data.dict())
    return create_room(db, room)
  
def get_all_rooms_use_case(db: Session):
    return get_all_rooms(db)
  
def get_room_by_id_use_case(db: Session, room_id: int):
    return get_room_by_id(db, room_id)

def update_room_use_case(db: Session, room_id: int, room_data: RoomUpdate):
    room_data.id = room_id
    return update_room(db, room_id, room_data)
  
def delete_room_use_case(db: Session, room_id: int):
    return delete_room(db, room_id)

