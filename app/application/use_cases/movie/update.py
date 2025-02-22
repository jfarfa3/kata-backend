from app.infrastructure.repositories.movie_repository import update_movie
from app.domain.models.movie import Movie

def execute(db, movie_id, movie_data):
    movie = Movie(**movie_data.dict())
    return update_movie(db, movie_id, movie)
