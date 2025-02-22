from sqlalchemy.orm import Session
from app.domain.models import Showtime
from datetime import datetime, timedelta

def get_showtimes_by_movie_id(db: Session, movie_id: int):
    return db.query(Showtime).filter(Showtime.movie_id == movie_id).all()

def get_showtime_by_room_id_and_time(db: Session, room_id: int, start_time: datetime):
    return db.query(Showtime).filter(Showtime.room_id == room_id, Showtime.start_time == start_time).first()

def create_showtime(db: Session, showtime: Showtime):
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime

def is_showtime_available(db: Session, room_id: int, new_start: datetime, new_end: datetime, break_time: int):
    overlapping = db.query(Showtime).filter(
        Showtime.room_id == room_id,
        Showtime.start_time < new_end,
        Showtime.end_time > new_start
    ).first()
    return overlapping is None