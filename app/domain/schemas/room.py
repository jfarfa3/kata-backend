from pydantic import BaseModel
from typing import Optional
from typing import List
from app.domain.schemas.seat import Seat


class RoomBase(BaseModel):
    name: str
    capacity: int
    break_time: int


class RoomCreate(RoomBase):
    pass


class RoomPatch(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    capacity: Optional[int] = None
    break_time: Optional[int] = None


class RoomUpdate(RoomPatch):
    pass


class RoomResponse(RoomBase):
    id: int
    seats: List[Seat]

    class Config:
        from_attributes = True
