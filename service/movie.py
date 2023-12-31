from dao.movie import MovieDAO
from model.movie import Movie
from service.director import DirectorService
from service.genre import GenreService


class MovieService:
    def __init__(self, dao: MovieDAO, genre_service: GenreService,
                 director_service: DirectorService):
        self.dao = dao
        self.genre_service = genre_service
        self.director_service = director_service

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        movie = Movie(**data)

        return self.dao.create(movie)

    def update(self, mid, data):
        return self.dao.update(mid, data)

    def delete(self, mid):
        return self.dao.delete(mid)
