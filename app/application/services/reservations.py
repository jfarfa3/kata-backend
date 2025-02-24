from sqlalchemy.orm import Session
from app.application.use_cases.showtime import get_showtime_by_id
from app.application.use_cases.movie import get_movie_by_id
from app.domain.models.movie import Movie
from app.application.use_cases.seats import save_seats_in_showtime
from app.domain.models.reservation import Reservation
from app.domain.models.showtime import Showtime
from app.domain.schemas.seat import SeatsCreate
from app.infrastructure.services.send_email import send_cancelled_reservation_email, send_confirmed_reservation_email

def cancel_reservation(db: Session, reservation: Reservation):
    showtime: Showtime | None = get_showtime_by_id(db, reservation.showtime_id)
    if showtime is None:
        raise ValueError("Showtime not found")
    
    movie: Movie| None = get_movie_by_id(db, showtime.movie_id)
    if movie is None:
        raise ValueError("Movie not found")
    
    
    updated_seats = [seat for seat in showtime.seats_sold if seat not in reservation.seats]
    seats_update = SeatsCreate(seats=updated_seats)
    save_seats_in_showtime(db, showtime.id, seats_update)
    send_cancelled_reservation_email(reservation, showtime, movie)
    return
  
def confirm_reservation(db: Session, reservation: Reservation):
    showtime: Showtime | None = get_showtime_by_id(db, reservation.showtime_id)
    if showtime is None:
        raise ValueError("Showtime not found")
    
    movie: Movie| None = get_movie_by_id(db, showtime.movie_id)
    if movie is None:
        raise ValueError("Movie not found")
    
    send_confirmed_reservation_email(reservation, showtime, movie)
    return