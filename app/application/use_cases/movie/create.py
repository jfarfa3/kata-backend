from app.infrastructure.repositories.movie_repository import create_movie
from app.domain.models.movie import Movie

def execute(db, movie_data):
    movie = Movie(**movie_data.dict())
    return create_movie(db, movie)