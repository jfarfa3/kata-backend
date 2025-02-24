from sqlalchemy.orm import Session
from app.domain.models import Showtime
from app.domain.schemas.seat import SeatsCreate

def get_showtime_by_id(db: Session, showtime_id: int):
    print("showtime_id", showtime_id)
    return db.query(Showtime).filter(Showtime.id == showtime_id).first()

def get_showtimes_by_movie_id(db: Session, movie_id: int):
    return db.query(Showtime).filter(Showtime.movie_id == movie_id).all()


def get_showtimes_by_room_id(db: Session, room_id: int):
    return db.query(Showtime).filter(Showtime.room_id == room_id).all()


def create_showtime(db: Session, showtime: Showtime):
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime

def save_seats_in_showtime(db: Session, showtime_id: int, seats: SeatsCreate):
    showtime = db.query(Showtime).filter(Showtime.id == showtime_id).first()
    if not showtime:
        return None
    seats_dic = [seat.dict() for seat in seats.seats]
    showtime.seats_sold = seats_dic
    db.commit()
    return showtime
