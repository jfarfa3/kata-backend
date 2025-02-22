from sqlalchemy.orm import Session
from app.domain.models.reservation import Reservation

def create_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def get_reservations_by_showtime_id(db: Session, showtime_id: int):
    return db.query(Reservation).filter(Reservation.showtime_id == showtime_id).all()

def get_reservation_by_user_email(db: Session, user_email: str):
    return db.query(Reservation).filter(Reservation.user_email == user_email).all()
