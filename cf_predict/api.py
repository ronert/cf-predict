from flask import Blueprint
import flask_restful
from .resources import Catalogue, Model


api_bp = Blueprint("api", __name__)
api = flask_restful.Api(api_bp)

api.add_resource(Catalogue, "/", endpoint="catalogue")
api.add_resource(Model, "/model", endpoint="model")
