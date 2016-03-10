from flask_restful import Resource, reqparse
from flask import url_for
import cf_predict


class Catalogue(Resource):
    def get(self):
        """Show a catalogue of available endpoints."""
        return {
            "predict_url": url_for("api.predict",
                                   _external=True),
            "model_version_url": url_for("api.model",
                                         _external=True),
            "api_version": cf_predict.__version__
        }


class Model(Resource):
    def get(self):
        """Get current model version."""
        return {"Version": "1.0"}

    def put(self):
        """Load a specific model version into memory from Redis.

        Either specifiy the model version or 'latest'.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("version", type=str, required=True)
        args = parser.parse_args()
        return args["version"]


class Predict(Resource):
    def get(self):
        """Get prediction from model.

        Input: Feature array
        """
        parser = reqparse.RequestParser()
        parser.add_argument("features", type=str, required=True)
        args = parser.parse_args()
        return args
