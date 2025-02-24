from sqlalchemy.orm import Session
from app.infrastructure.repositories.movie_repository import create_movie, update_movie, get_all_movies, get_movie_by_id, delete_movie
from app.domain.models.movie import Movie
from app.domain.schemas.movie import MovieUpdate, MovieCreate

def create_movie_use_case(db: Session, movie_data: MovieCreate):
    movie = Movie(**movie_data.dict())
    return create_movie(db, movie)
  
def update_movie_use_case(db: Session, movie_id: int, movie_data: MovieUpdate):
    movie_data.id = movie_id
    return update_movie(db, movie_id, movie_data)
  
def get_all_movies_use_case(db: Session):
    return get_all_movies(db)
  
def get_movie_by_id_use_case(db: Session, movie_id: int):
    return get_movie_by_id(db, movie_id)

def delete_movie_use_case(db: Session, movie_id: int):
    return delete_movie(db, movie_id)