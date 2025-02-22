from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases.movie import create, update, list, delete
from app.infrastructure.database import get_db
from app.domain.schemas.movie import MovieCreate, MovieUpdate

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/")
def add_movie(movie_data: MovieCreate, db = Depends(get_db)):
    try:
        return create.execute(db, movie_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/")
def get_movies(db = Depends(get_db)):
    try:
        return list.execute(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{movie_id}")
def get_movie(movie_id: int, db = Depends(get_db)):
    try:
        return list.execute(db, movie_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{movie_id}")
def update_movie(movie_id: int, movie_data: MovieUpdate, db = Depends(get_db)):
    try:
        return update.execute(db, movie_id, movie_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))