from flask import Flask
from flask_restx import Resource, Namespace

from container import movie_service
from model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesVies(Resource):

    def get(self):
        return 'hello world'


@movie_ns.route('/<int:mid>')
class MoviesVies(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200
