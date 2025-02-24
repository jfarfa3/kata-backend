from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases.reservation import create_reservation_use_case, get_all_reservations_use_case, get_reservation_by_user_email_use_case, get_reservations_by_showtime_id_use_case, update__state_reservation_use_case, delete_reservation_use_case
from app.application.use_cases.seats import save_seats_in_reservation_use_case
from app.infrastructure.database import get_db
from app.domain.schemas.reservation import ReservationCreate, ReservationResponse
from app.domain.enums import ReservationState
from app.domain.schemas.seat import SeatsCreate
from starlette.status import HTTP_204_NO_CONTENT


router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post(
    "/",
    response_model=ReservationResponse,
    description="Add a new reservation",
)
def add_reservation(reservation_data: ReservationCreate, db=Depends(get_db)):
    try:
        return create_reservation_use_case(db, reservation_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/",
    response_model=List[ReservationResponse],
    description="Get all reservations",
)
def get_reservations(db=Depends(get_db)):
    try:
        return get_all_reservations_use_case(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/user/{user_email}",
    response_model=List[ReservationResponse],
    description="Get all reservations by user email",
)
def get_reservations_by_user_email(user_email: str, db=Depends(get_db)):
    try:
        return get_reservation_by_user_email_use_case(db, user_email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/showtime/{showtime_id}",
    response_model=List[ReservationResponse],
    description="Get all reservations by showtime id",
)
def get_reservations_by_showtime_id(showtime_id: int, db=Depends(get_db)):
    try:
        return get_reservations_by_showtime_id_use_case(db, showtime_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    "/{reservation_id}/{new_state}",
    response_model=ReservationResponse,
    description="Update a reservation",
)
def update_reservation(reservation_id: int, new_state: ReservationState, db=Depends(get_db)):
    try:
        return update__state_reservation_use_case(db, reservation_id, new_state)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete(
    "/{reservation_id}",
    description="Delete a reservation",
    status_code=HTTP_204_NO_CONTENT
)
def delete_reservation(reservation_id: int, db=Depends(get_db)):
    try:
        delete_reservation_use_case(db, reservation_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch(
    "/{reservation_id}/seats",
    description="Save or update seats in a reservation",
    status_code=HTTP_204_NO_CONTENT
)
def save_seats(reservation_id: int, seats_data: SeatsCreate, db=Depends(get_db)):
    try:
        save_seats_in_reservation_use_case(db, reservation_id, seats_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
