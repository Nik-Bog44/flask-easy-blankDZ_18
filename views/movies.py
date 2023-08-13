from flask import Flask, request
from flask_restx import Resource, Namespace

from container import movie_service
from model.genre import GenreSchema
from model.movie import MovieSchema
from service.genre import GenreService

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@movie_ns.route('/')
class MoviesVies(Resource):

    def get(self):
        movie = movie_service.get_all()
        return movie_schema.dump(movie), 200


@movie_ns.route('/<int:mid>')
class MoviesVies(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200


@movie_ns.route('/director/<int:director_id>')
class MoviesVies(Resource):
    def get(self, director_id):
        movie = movie_service.get_by_director(director_id)
        return movie_schema.dump(movie), 200


@movie_ns.route('/genre/<int:genre_id>')
class MoviesByGenreView(Resource):

    def get(self, genre_id):
        movies = GenreService.get_one(genre_id)
        return genre_schema.dump(movies), 200


@movie_ns.route('/year<int:year>')
class MoviesVies(Resource):

    def get(self, year):
        movie = movie_service.get_by_year(year)
        return movie_schema.dump(movie), 200


@movie_ns.route('/movies')
class MoviesVies(Resource):
    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return movie_schema.dump(movie), 201


@movie_ns.route('/movies/<int:mid>')
class MoviesVies(Resource):
    def put(self, mid):
        movie = movie_service.create(mid)
        return movie_schema.dump(movie), 201


@movie_ns.route('/<int:mid>')
class MoviesVies(Resource):

    def delete(self, mid):
        movie = movie_service.delete(mid)
        return movie_schema.dump(movie), 200
