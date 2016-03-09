from flask.ext.redis import FlaskRedis
from flask.ext.restful import Resource, reqparse
import cf_predict
from flask import url_for


class Catalogue(Resource):
    def get(self):
        return {
            "predict_url": url_for("api.predict", _external=True),
            "model_version_url": url_for("api.model", _external=True),
            "api_version": cf_predict.__version__
        }


class Model(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("version", type=str, required=True)

    def get(self):
        return {"Version": "1.0"}

    def put(self):
        args = self.parser.parse_args()
        return args["version"]


class Predict(Resource):
    def get(self):
        pass
