from flask.ext.restful import Resource, reqparse
import cf_predict
from flask import url_for


class Catalogue(Resource):
    def get(self):
        return {
            "predict_url": url_for("api.predict", _external=True),
            "model_version_url": url_for("api.get_model", _external=True),
            "api_version": cf_predict.__version__
        }


class Model(Resource):
    def __init__(self):
        # TODO: only example code
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, required=True,
                                   help="No task title provided", location="json")
        self.reqparse.add_argument("description", type=str, default="", location="json")
        super(ModelVersion, self).__init__()

    def get(self):
        return {"Version": "1.0"}

    def put(self, version):
        args = self.reqparse.parse_args()


class Predict(Resource):
    def get(self):
        pass
