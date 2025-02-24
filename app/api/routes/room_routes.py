from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases.room import create_room_use_case, get_all_rooms_use_case, get_room_by_id_use_case, update_room_use_case, delete_room_use_case
from app.application.use_cases.seats import save_seats_in_room_use_case
from app.infrastructure.database import get_db
from app.domain.schemas.room import RoomCreate, RoomUpdate, RoomResponse
from app.domain.schemas.seat import SeatsCreate
from starlette.status import HTTP_204_NO_CONTENT

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.post(
    "/",
    response_model=RoomResponse,
    description="Add a new room",
)
def add_room(room_data: RoomCreate, db=Depends(get_db)):
    try:
        return create_room_use_case(db, room_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/",
    response_model=List[RoomResponse],
    description="Get all rooms",
)
def get_rooms(db=Depends(get_db)):
    try:
        return get_all_rooms_use_case(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{room_id}",
    response_model=RoomResponse,
    description="Get a room by id",
)
def get_room(room_id: int, db=Depends(get_db)):
    try:
        return get_room_by_id_use_case(db, room_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(
    "/{room_id}",
    response_model=RoomResponse,
    description="Update a room",
)
def update_room(room_id: int, room_data: RoomUpdate, db=Depends(get_db)):
    try:
        return update_room_use_case(db, room_id, room_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(
    "/{room_id}",
    description="Delete a room",
    status_code=HTTP_204_NO_CONTENT
)
def delete_room(room_id: int, db=Depends(get_db)):
    try:
        delete_room_use_case(db, room_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch(
    "/{room_id}/seats",
    description="Save or update seats in a room",
    status_code=HTTP_204_NO_CONTENT
)
def save_seats(room_id: int, seats_data: SeatsCreate, db=Depends(get_db)):
    try:
        save_seats_in_room_use_case(db, room_id, seats_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
