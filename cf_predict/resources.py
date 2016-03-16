import pickle
import os
from flask_restful import Resource, reqparse
from flask import url_for, current_app
import cf_predict


def get_db():
    """Fetch Redis client."""
    return current_app.extensions["redis"]


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
    def __init__(self):
        self.r = get_db()
        self.version = os.getenv("MODEL_VERSION") or "latest"
        if self.version == "latest":
            try:
                self.version = self.find_latest_version(self.version)
                self.model = self.load_model(self.version)
            except (TypeError, ValueError):
                current_app.logger.warning("No model {} found".format(self.version))

    def find_latest_version(self, version):
        """Find model with the highest version number in Redis."""
        latest_version = max(self.r.keys())
        return latest_version

    def load_model(self, version):
        """Deserialize and load model."""
        return pickle.loads(self.r.get(version))

    def get(self):
        """Get current model version."""
        return {"model_version": self.version}

    def put(self):
        """Load a specific model version into memory from Redis.

        Either specifiy the model version or 'latest'.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("version", type=str, required=True)
        args = parser.parse_args()
        version = args["version"]
        try:
            if version == "latest":
                self.version = self.find_latest_version(version)
            else:
                self.version = version
                self.model = self.load_model(self.version)
            return {"model_version": self.version}
        except (TypeError, ValueError):
            message = {"message": "Model version {} not found".format(version)}
            current_app.logger.warning(message)
            return message, 404


class Predict(Resource):
    def get(self):
        """Get prediction from model.

        Input: Feature array
        """
        parser = reqparse.RequestParser()
        parser.add_argument("features", type=str, required=True)
        args = parser.parse_args()
        return args
