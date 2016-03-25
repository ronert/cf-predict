"""Unit test cf_predict"""
import json
import pickle

import numpy as np
import pytest

from mockredis import MockRedis
from .conftest import models
from cf_predict import __version__
from cf_predict.resources import get_db
from cf_predict.errors import NoPredictMethod


@pytest.mark.usefixtures("client_class")
class TestCf_predict:
    def test_catalogue(self):
        rv = self.client.get("/")
        assert rv.status_code == 200
        assert rv.json == {
            "model_url": "http://localhost/model",
            "api_version": __version__
        }

    def test_get_db(self):
        r = get_db()
        r.set("test", 5)
        assert int(r.get("test")) == 5

    def test_no_model_in_db(self, monkeypatch, caplog):
        monkeypatch.setattr("cf_predict.resources.get_db", MockRedis)
        pytest.raises(ValueError, self.client.get, "/model")
        assert "No model" in caplog.text()

    def test_model_pickle_error(self, monkeypatch, caplog):
        def broken_pickle(anything):
            raise IOError
        monkeypatch.setattr("pickle.loads", broken_pickle)
        pytest.raises(IOError, self.client.get, "/model")

    def test_model_no_predict_error(self, monkeypatch, caplog, broken_model):
        monkeypatch.setattr("cf_predict.resources.get_db", broken_model)
        pytest.raises(NoPredictMethod, self.client.get, "/model")

    def test_get_version(self):
        rv = self.client.get("/model")
        assert rv.status_code == 200
        assert rv.json == {
            "model_version": "1.2.0"
        }

    def test_post_prediction_valid_features(self):
        features = {"features": [1, 2, 3, 4, 5]}
        model = pickle.loads(models().get("1.2.0"))
        rv = self.client.post("/model",
                              data=json.dumps(features),
                              content_type="application/json")
        assert rv.status_code == 200
        assert rv.json == {
            "model_version": "1.2.0",
            "prediction": list(model.predict(np.array(features["features"]).reshape(1, -1)))
        }

    def test_post_prediction_invalid_features(self):
        features = {"features": [1, 2, "lol", 4, 5]}
        rv = self.client.post("/model",
                              data=json.dumps(features),
                              content_type="application/json")
        assert rv.status_code == 400
        assert rv.json == {
            "message": "Features [1, 2, 'lol', 4, 5] do not match expected input for model version 1.2.0"
        }
