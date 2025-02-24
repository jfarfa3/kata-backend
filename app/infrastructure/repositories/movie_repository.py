import logging
from sqlalchemy.orm import Session
from app.domain.models import Movie

logger = logging.getLogger('uvicorn.error')

def get_all_movies(db: Session):
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def create_movie(db: Session, movie: Movie):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def update_movie(db: Session, movie_id: int, movie: Movie):
    try:
        db.query(Movie).filter(Movie.id == movie_id).update(movie.dict())
        db.commit()
    except Exception as e:
        raise e
    return movie

def delete_movie(db: Session, movie_id: int):
    try:
        room = db.query(Movie).filter(Movie.id == movie_id).first()
        if not room:
            return None        
        db.delete(room)
        db.commit()
        return room
        
    except Exception as e:
        db.rollback()
        raise e

