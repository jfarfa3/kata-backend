from app.infrastructure.repositories.movie_repository import delete_movie

def execute(db, movie):
    return delete_movie(db, movie)