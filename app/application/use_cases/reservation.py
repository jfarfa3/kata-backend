from sqlalchemy.orm import Session
from app.infrastructure.repositories.reservation_repository import create_reservation, get_all_reservations, get_reservation_by_user_email, get_reservations_by_showtime_id, update_state_reservation, delete_reservation
from app.domain.models.reservation import Reservation
from app.domain.schemas.reservation import ReservationCreate, ReservationUpdate
from app.domain.enums import ReservationState
from app.application.services.reservations import cancel_reservation, confirm_reservation
from app.domain.models.showtime import Showtime


def create_reservation_use_case(db: Session, reservation: ReservationCreate):
    reservation = Reservation(**reservation.dict())
    return create_reservation(db, reservation)
  
def get_reservations_by_showtime_id_use_case(db: Session, showtime_id: int):
    return get_reservations_by_showtime_id(db, showtime_id)

def get_reservation_by_user_email_use_case(db: Session, user_email: str):
    return get_reservation_by_user_email(db, user_email)

def get_all_reservations_use_case(db: Session):
    return get_all_reservations(db)

def get_reservation_by_id_use_case(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def update__state_reservation_use_case(db: Session, reservation_id: int, new_state: ReservationUpdate):
    reservation: Reservation | None = get_reservation_by_id_use_case(db, reservation_id)
    if reservation is None:
        raise ValueError("Reservation not found")
    if new_state is ReservationState.CANCELLED:
        cancel_reservation(db, reservation)
    if new_state is ReservationState.CONFIRMED:
        confirm_reservation(db, reservation)
        
    return update_state_reservation(db, reservation_id, new_state)
  
def delete_reservation_use_case(db: Session, reservation_id: int):
    return delete_reservation(db, reservation_id)

  

