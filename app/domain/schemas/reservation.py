from pydantic import BaseModel
from typing import Optional
from typing import List
from app.domain.schemas.seat import Seat
from app.domain.enums import ReservationState


class ReservationBase(BaseModel):
    user_name: str
    user_email: str
    user_phone: str
    showtime_id: int


class ReservationCreate(ReservationBase):
    pass


class ReservationPatch(BaseModel):
    id: Optional[int] = None
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    user_phone: Optional[str] = None
    showtime_id: Optional[int] = None


class ReservationUpdate(ReservationPatch):
    pass


class ReservationResponse(ReservationBase):
    id: int
    state: ReservationState
    seats: List[Seat]

    class Config:
        from_attributes = True
