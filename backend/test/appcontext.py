import pytest

from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    return app