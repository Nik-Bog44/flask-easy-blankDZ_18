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
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        datas = {
            "director_id": director_id,
            "genre_id": genre,
            "year": year,
        }
        movies_all = movie_service.get_all(datas)

        return movies_schema.dump(movies_all), 200

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return movie_schema.dump(movie), 201


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
