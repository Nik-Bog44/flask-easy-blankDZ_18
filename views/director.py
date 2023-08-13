from flask_restx import Resource, Namespace

from container import director_service
from model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
movies_schemas = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorVies(Resource):

    def get(self):
        movie = director_service.get_all()
        return director_schema.dump(movie), 200


@director_ns.route('/<int:mid>')
class DirectorVies(Resource):

    def get(self, did):
        movie = director_service.get_one(did)
        return director_schema.dump(movie), 200
