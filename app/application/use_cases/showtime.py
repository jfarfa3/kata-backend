from sqlalchemy.orm import Session
from app.domain.schemas.showtime import ShowtimeCreate
from app.domain.models.showtime import Showtime
from app.infrastructure.repositories.showtime_repository import create_showtime, get_showtimes_by_movie_id, get_showtimes_by_room_id, get_showtime_by_id

def create_showtime_use_case(db: Session, showtime_data: ShowtimeCreate):
    showtime = Showtime(**showtime_data.dict())
    return create_showtime(db, showtime)
  
def get_showtimes_by_movie_id_use_case(db: Session, movie_id: int):
    return get_showtimes_by_movie_id(db, movie_id)
  
def get_showtimes_by_room_id_use_case(db: Session, room_id: int):
    return get_showtimes_by_room_id(db, room_id)

def get_showtime_by_id_use_case(db: Session, showtime_id: int):
    return get_showtime_by_id(db, showtime_id)
    