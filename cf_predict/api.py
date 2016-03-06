from flask import Flask, Blueprint
from .resources import HelloWorld, ModelVersion, Predict
import flask.ext.redis
import flask.ext.restful as flask_restful


api_bp = Blueprint("api", __name__)
api = flask_restful.Api(api_bp)


api.add_resource(HelloWorld, "/helloworld")
api.add_resource(ModelVersion, "/model_version<int:version>")
api.add_resource(Predict, "/predict")
