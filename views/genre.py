
from flask_restx import Resource, Namespace

from container import genre_service
from model.genre import GenreSchema


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)


@genre_ns.route('/')
class GenreVies(Resource):

    def get(self):
        movie = genre_service.get_all()
        return genre_schemas.dump(movie), 200


@genre_ns.route('/<int:gid>')
class GenreVies(Resource):

    def get(self, gid):
        movie = genre_service.get_one(gid)
        return genre_schema.dump(movie), 200