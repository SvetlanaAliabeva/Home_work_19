from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route("/")
class DirectorsView(Resource):

    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(all_directors)

        return result, 200

    @admin_required
    def post(self):
        requst_json = request.json
        director = director_service.create(requst_json)
        return "", 201, {"location": f"/genres/{director.id}"}


@director_ns.route("/<int:uid>")
class DirectorView(Resource):

    @auth_required
    def get(self, uid):
        director = director_service.get_one(uid)
        result = DirectorSchema().dump(director)

        return result, 200

    @admin_required
    def put(self, did):
        request_json = request.json
        if "id" not in request_json:
            request_json['id'] = did

        director_service.update(request_json)
        return  "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
