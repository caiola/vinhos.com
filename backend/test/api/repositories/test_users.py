import pytest
from sqlalchemy.exc import IntegrityError

from api.repositories import users


def test_success_create_user(session, faker):
    """Successfully creates users with correct attributes"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    user = users.create(first_name, last_name)
    assert user.id
    assert user.first_name == first_name
    assert user.last_name == last_name


def test_can_be_multiple_user_same_attributes(session, faker):
    """There can be users with same attributes"""
    first_name = faker.first_name()
    last_name = faker.last_name()
    user_1 = users.create(faker.first_name(), faker.last_name())
    user_2 = users.create(faker.first_name(), faker.last_name())
    assert user_1.id != user_2.id


def test_user_must_have_first_name(session, faker):
    """Test user must have a first name"""
    with pytest.raises(IntegrityError):
        users.create(faker.first_name(), None)


def test_user_must_have_last_name(session, faker):
    """Test user must have a last name"""

    with pytest.raises(IntegrityError):
        users.create(None, faker.last_name())
