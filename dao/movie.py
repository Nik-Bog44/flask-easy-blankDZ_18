from model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

    def update(self,mid):
        movie = self.get_one(mid.get("id"))
        movie.title = mid.get("title")
        movie.description = mid.get("description")
        movie.trailer = mid.get("trailer")
        movie.year = mid.get("year")
        movie.genre_id = mid.get("genre_id")
        movie.director_id = mid.get("director_id")

        self.session.add(movie)
        self.session.commit()

        return movie
