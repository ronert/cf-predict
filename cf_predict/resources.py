from flask.ext.restful import Resource
from flask.ext.restful import reqparse


class HelloWorld(Resource):
    def get(self):
        return {
            "hello": "world",
            "version": "1"
        }


class ModelVersion(Resource):
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
