from pydantic import BaseModel
from typing import List

class Seat(BaseModel):
    row: int
    number: int
    
class SeatsCreate(BaseModel):
    seats: List[Seat]