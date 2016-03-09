from flask import Blueprint
from .resources import Catalogue, Model, Predict
# import flask.ext.redis
import flask.ext.restful as flask_restful


api_bp = Blueprint("api", __name__)
api = flask_restful.Api(api_bp)


api.add_resource(Catalogue, "/", endpoint="catalogue")
api.add_resource(Model, "/model", endpoint="model")
api.add_resource(Predict, "/predict", endpoint="predict")
