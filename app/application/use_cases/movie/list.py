from app.infrastructure.repositories.movie_repository import get_all_movies, get_movie_by_id

def execute(db, movie_id):
    if movie_id:
        return get_movie_by_id(db, movie_id)
    else:
      return get_all_movies(db)