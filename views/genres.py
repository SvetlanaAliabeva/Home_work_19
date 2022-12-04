from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from decorators import auth_required, admin_required

genre_ns = Namespace('genres')

@genre_ns.route("/")
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(all_genres)
        return result, 200

    @admin_required
    def post(self):
        requst_json = request.json
        genre = genre_service.create(requst_json)
        return "", 201, {"location": f"/genres/{genre.id}"}

@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        genre = genre_service.get_one(uid)
        result = GenreSchema().dump(genre)
        return result, 200

    @admin_required
    def put(self, gid):
        request_json = request.json
        if "id" not in request_json:
            request_json['id'] = gid

        genre_service.update(request_json)
        return  "", 204

    @admin_required
    def delete(self, uid):
        genre_service.delete(uid)
        return "", 204
