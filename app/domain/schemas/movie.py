from app.domain.enums import MovieFormat
from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    title: str
    genre: str
    duration: int
    classification: str
    format: MovieFormat

class MovieCreate(MovieBase):
    pass

class MoviePatch(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    genre: Optional[str] = None
    duration: Optional[int] = None
    classification: Optional[str] = None
    format: Optional[MovieFormat] = None

class MovieUpdate(MoviePatch):
    pass

class MovieResponse(MovieBase):
    id: int
    
    class Config:
        from_attributes = True