from pydantic import BaseModel
from typing import Optional
from typing import List
from app.domain.schemas.seat import Seat


class ShowtimeBase(BaseModel):
    movie_id: int
    room_id: int
    start_time: str
    end_time: str
    
class ShowtimeCreate(ShowtimeBase):
    pass
  
class ShowtimePatch(BaseModel):
    id: Optional[int] = None
    movie_id: Optional[int] = None
    room_id: Optional[int] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None

class ShowtimeUpdate(ShowtimePatch):
    pass
  
class ShowtimeResponse(ShowtimeBase):
    id: int
    seats_sold: List[Seat]
    
    class Config:
        from_attributes = True
    
    