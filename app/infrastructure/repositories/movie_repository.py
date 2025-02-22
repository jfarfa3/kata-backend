from sqlalchemy.orm import Session
from app.domain.models import Movie

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
    db.query(Movie).filter(Movie.id == movie_id).update(movie.dict())
    db.commit()
    return movie

def delete_movie(db: Session, movie: Movie):
    db.delete(movie)
    db.commit()
    return movie

