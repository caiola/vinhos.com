import pytest
import uuid
from sqlalchemy.exc import IntegrityError

from api.models import Ad, User
from api.repositories import ads


@pytest.fixture()
def user(faker):
    """A fake user"""
    return User(first_name=faker.first_name(), last_name=faker.last_name()).save()


@pytest.fixture()
def description(faker):
    """Fake description"""
    return faker.text()


@pytest.fixture()
def title(faker):
    """Fake title"""
    return faker.text()[0:10]


def test_create_ad_success(session, user, description, title):
    """When creating a successfully add all fields should be present"""

    ad = ads.create(user, title, description)
    assert ad.id
    assert ad.user == user
    assert ad.description == description
    assert ad.title == title
    assert isinstance(ad.uuid, uuid.UUID)


def test_fail_create_ad_without_client(session, user, description, title):
    """When a add has no client it fails to create"""
    with pytest.raises(IntegrityError):
        ad = ads.create(None, title, description)


def test_fail_create_add_without_title(session, user, description):
    """Fails to create add without a title"""
    with pytest.raises(IntegrityError):
        ads.create(user, None, description)


def test_fail_create_ad_without_description(session, user, title):
    """Fails to create add without description"""
    with pytest.raises(IntegrityError):
        ad = ads.create(user, title, description=None)


def test_fail_create_add_duplicate_title(session, user, title, description):
    """Fails to create an add with duplicate title"""

    ad = Ad(user_id=user.id, title=title, description=description).save()
    with pytest.raises(IntegrityError):
        ad = ads.create(user, title, description)
