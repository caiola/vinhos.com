import pytest
import uuid
from flask_migrate import upgrade as flask_migrate_upgrade

from api import create_app
from api.models import db as _db
from test.factories import AdFactory


@pytest.fixture(scope="session")
def app():
    """Generate an app instance"""
    app = create_app(True)

    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def db(app, request):
    """Session-wide test database."""

    def teardown():
        _db.drop_all()

    _db.app = app

    # flask_migrate_upgrade(directory="migrations")
    _db.create_all()
    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def session(db, request):
    db.session.begin_nested()

    def commit():
        db.session.flush()

    # patch commit method
    old_commit = db.session.commit
    db.session.commit = commit

    def teardown():
        db.session.rollback()
        db.session.close()
        db.session.commit = old_commit

    request.addfinalizer(teardown)
    return db.session


@pytest.fixture()
def ad(session):
    return AdFactory.create()


@pytest.fixture()
def random_uuid():
    return uuid.uuid4()
