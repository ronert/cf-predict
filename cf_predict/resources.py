import pickle
import os
from flask import url_for, current_app
import cf_predict


def get_db():
    """Fetch Redis client."""
    return current_app.extensions["redis"]


class Catalogue(Resource):
    def get(self):
        """Show a catalogue of available endpoints."""
        return {
            "model_url": url_for("api.model", _external=True),
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
	keys = [key.decode("utf-8") for key in self.r.scan_iter()]
        latest_version = max(keys)
        return latest_version

    def load_model(self, version):
        """Deserialize and load model."""
        return pickle.loads(self.r.get(version))

    def get(self):
        """Get current model version."""
        return {"model_version": self.version}

    def post(self):
        """Get prediction from model.

        Input: Feature array
        """
        if self.model:
            prediction = {"prediction": self.model.predict(features)}
            return prediction
        else:
            message = {"message": "No model found"}
            return message, 404
