from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.domain.schemas.showtime import ShowtimeResponse, ShowtimeCreate
from starlette.status import HTTP_204_NO_CONTENT
from app.application.use_cases.showtime import create_showtime_use_case, get_showtimes_by_movie_id_use_case, get_showtimes_by_room_id_use_case, get_showtime_by_id_use_case
from app.application.use_cases.seats import save_seats_in_showtime_use_case
from app.infrastructure.database import get_db
from app.domain.schemas.seat import SeatsCreate

router = APIRouter(prefix="/showtimes", tags=["Showtimes"])


@router.post(
    "/",
    response_model=ShowtimeResponse,
    description="Add a new showtime",
)
def add_showtime(showtime_data: ShowtimeCreate, db=Depends(get_db)):
    try:
        return create_showtime_use_case(db, showtime_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{showtime_id}",
    response_model=ShowtimeResponse,
    description="Get showtime by id",
)
def get_showtime_by_id(showtime_id: int, db=Depends(get_db)):
    return get_showtime_by_id_use_case(db, showtime_id)


@router.get(
    "/movie/{movie_id}",
    response_model=List[ShowtimeResponse],
    description="Get showtimes by movie id",
)
def get_showtimes_by_movie_id(movie_id: int, db=Depends(get_db)):
    return get_showtimes_by_movie_id_use_case(db, movie_id)


@router.get(
    "/room/{room_id}",
    response_model=List[ShowtimeResponse],
    description="Get showtimes by room id",
)
def get_showtimes_by_room_id(room_id: int, db=Depends(get_db)):
    return get_showtimes_by_room_id_use_case(db, room_id)


@router.patch(
    "/{showtime_id}/seats",
    status_code=HTTP_204_NO_CONTENT,
    description="Save or Update seats in a showtime",
)
def save_seats_in_showtime(showtime_id: int, seats_data: SeatsCreate, db=Depends(get_db)):
    try:
        save_seats_in_showtime_use_case(db, showtime_id, seats_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
