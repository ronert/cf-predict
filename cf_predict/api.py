from flask import Flask, Blueprint
import flask_redis
import flask_restful


api_bp = Blueprint("api", __name__)
api = flask_restful.Api(api_bp)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
            "hello": "world",
            "version": "1"
        }

api.add_resource(HelloWorld, "/helloworld")
