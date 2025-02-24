import logging
from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases.movie import create_movie_use_case, get_all_movies_use_case, get_movie_by_id_use_case, update_movie_use_case, delete_movie_use_case
from app.infrastructure.database import get_db
from app.domain.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from starlette.status import HTTP_204_NO_CONTENT

logger = logging.getLogger('uvicorn.error')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
 )
console_handler.setFormatter(formatter)

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post(
        "/",
        response_model=MovieResponse,
        description="Add a new movie",
)
def add_movie(movie_data: MovieCreate, db = Depends(get_db)):
    try:
        return create_movie_use_case(db, movie_data)
    except Exception as e:
        logger.error(f"Error adding movie: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get(
        "/",
        response_model=list[MovieResponse],
        description="Get all movies",
)
def get_movies(db = Depends(get_db)):
    try:
        return get_all_movies_use_case(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get(
        "/{movie_id}",
        response_model=MovieResponse,
        description="Get a movie by id",
)
def get_movie(movie_id: int, db = Depends(get_db)):
    try:
        return get_movie_by_id_use_case(db, movie_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put(
        "/{movie_id}",
        response_model=MovieResponse,
        description="Update a movie",
)
def update_movie(movie_id: int, movie_data: MovieUpdate, db = Depends(get_db)):
    try:
        result = update_movie_use_case(db, movie_id, movie_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete(
        "/{movie_id}",
        description="Delete a movie",
    status_code=HTTP_204_NO_CONTENT
)
def delete_movie(movie_id: int, db = Depends(get_db)):
    try:
        delete_movie_use_case(db, movie_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))