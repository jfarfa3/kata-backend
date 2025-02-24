from sqlalchemy.orm import Session
from app.domain.models.reservation import Reservation
from app.domain.enums import ReservationState
from app.domain.schemas.seat import SeatsCreate


def create_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


def get_reservations_by_showtime_id(db: Session, showtime_id: int):
    return db.query(Reservation).filter(Reservation.showtime_id == showtime_id).all()


def get_reservation_by_user_email(db: Session, user_email: str):
    return db.query(Reservation).filter(Reservation.user_email == user_email).all()


def save_seats_in_reservation(db: Session, reservation_id: int, seats: SeatsCreate):
    reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id).first()
    if not reservation:
        return None
    seats_dic = [seat.dict() for seat in seats.seats]
    reservation.seats = seats_dic
    db.commit()
    return reservation


def update_state_reservation(db: Session, reservation_id: int, new_state: ReservationState):
    reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id).first()
    reservation.state = new_state
    db.commit()
    db.refresh(reservation)
    return reservation


def get_all_reservations(db: Session):
    return db.query(Reservation).all()


def delete_reservation(db: Session, reservation_id: int):
    try:
        reservation = db.query(Reservation).filter(
            Reservation.id == reservation_id).first()
        if not reservation:
            return None
        db.delete(reservation)
        db.commit()
        return reservation
    except Exception as e:
        db.rollback()
        raise e
