from model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

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

    def update(self,mid, data):
        movie = self.get_one(mid)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.session.add(movie)
        self.session.commit()

        return movie
