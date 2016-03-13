"""Unit tests configuration file."""
import pickle

import numpy as np
import pytest
from sklearn import linear_model, tree, svm

from cf_predict import create_app


def pytest_configure(config):
    """Disable verbose output when running tests."""
    terminal = config.pluginmanager.getplugin('terminal')
    base = terminal.TerminalReporter

    class QuietReporter(base):
        """A py.test reporting that only shows dots when running tests."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.verbosity = 0
            self.showlongtestinfo = False
            self.showfspath = False

    terminal.TerminalReporter = QuietReporter


@pytest.fixture
def app(monkeypatch):
    """Create a Flask test client."""
    monkeypatch.setattr("cf_predict.resources.get_db", models)
    app = create_app("unit_testing")
    return app


def models():
    """Create some sample machine learning models."""
    X = np.random.random_sample((20, 5))
    y = np.random.random_sample(20)
    lm = linear_model.LinearRegression()
    dt = tree.DecisionTreeRegressor()
    svr = svm.SVR()
    lm.fit(X, y)
    dt.fit(X, y)
    svr.fit(X, y)
    return {"1.0.0": pickle.dumps(lm),
            "1.1.0": pickle.dumps(dt),
            "1.2.0": pickle.dumps(svr)}
