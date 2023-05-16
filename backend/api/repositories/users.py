""" Defines the User repository """
import uuid

from api.models import User


def get_by(pk: int = None, uuid: uuid.UUID = None) -> User:
    """Query a user by uuid or id"""

    params = {}
    if (not pk and not uuid) or (pk and uuid):
        raise ValueError("Provide pk or uuid")

    if uuid:
        params["uuid"] = str(uuid)

    if pk:
        params["pk"] = pk

    return User.query.filter_by(**params).one()


def update(user: User, **kwargs) -> User:
    """Update a user's age"""
    user.update(kwargs)
    return user.save()


def create(first_name: str, last_name: str) -> User:
    """Create a new user"""
    user = User(first_name=first_name, last_name=last_name)

    return user.save()
