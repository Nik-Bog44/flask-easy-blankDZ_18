from flask import Flask, request
from flask_restx import Resource, Namespace

from container import movie_service
from model.genre import GenreSchema
from model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@movie_ns.route('/')
class MoviesVies(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        year = request.args.get("year")

        if director_id:
            if director_id == "15":
                movie = movie_service.get_by_director(director_id=15)
            else:
                movie = movie_service.get_by_director(director_id)
        elif year:
            if year == "2007":
                movie = movie_service.get_by_year(year=2007)
            else:
                movie = movie_service.get_by_year(year)
        else:
            movie = movie_service.get_all()
        return movies_schema.dump(movie), 200

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return movie_schema.dump(movie), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        return movies_schema.dump(movie), 200


@movie_ns.route('/director/<int:director_id>')
class MoviesVies(Resource):
    def get(self, director_id):
        movie = movie_service.get_by_director(director_id)

        return movies_schema.dump(movie), 200


@movie_ns.route('/year<int:year>')
class MoviesVies(Resource):

    def get(self, year):
        movie = movie_service.get_by_year(year)

        return movie_schema.dump(movie), 200


@movie_ns.route('/<int:mid>')
class MoviesVies(Resource):

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie = movie_service.update(mid, data)
        return movie_schema.dump(movie), 201

    def delete(self, mid):
        movie = movie_service.delete(mid)
        return movie_schema.dump(movie), 200
