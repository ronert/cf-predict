"""Unit test cf_predict"""
import pytest
from cf_predict import __version__


@pytest.mark.usefixtures("client_class")
class TestCf_predict:
    def test_catalogue(self):
        rv = self.client.get("/")
        assert rv.status_code == 200
        assert rv.json == {
            "predict_url": "http://localhost/predict",
            "model_version_url": "http://localhost/model",
            "api_version": __version__
        }

    def test_put_version_valid(self):
        rv = self.client.put("/model?version=latest")
        assert rv.status_code == 200
        assert rv.json == {
            "model_version": "1.0.0"
        }

    def test_put_version_invalid(self):
        pass

    def test_get_version_valid(self):
        pass

    def test_get_version_invalid(self):
        pass

    def test_get_prediction_valid_input(self):
        pass

    def test_get_prediction_invalid_id(self):
        pass

    def test_get_prediction_invalid_features(self):
        pass

    def test_get_prediction_valid_json_output(self):
        pass
