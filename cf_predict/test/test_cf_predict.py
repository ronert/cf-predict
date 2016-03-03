"""Unit test cf_predict"""
import pytest


@pytest.mark.usefixtures("client_class")
class TestCf_predict:
    def test_connection(self):
        rv = self.client.get("/")
        assert rv.status_code == 200
        assert "Connection Success" in rv.get_data(as_text=True)

    def test_get_root(self):
        pass

    def test_get_prediction_valid_input(self):
        pass

    def test_get_prediction_invalid_id(self):
        pass

    def test_get_prediction_invalid_features(self):
        pass

    def test_get_prediction_valid_json_output(self):
        pass

    def test_get_version_valid(self):
        pass

    def test_get_version_invalid(self):
        pass

    def test_put_version_valid(self):
        pass

    def test_put_version_invalid(self):
        pass
