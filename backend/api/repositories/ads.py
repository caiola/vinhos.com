""" Defines the Ad repository """
import uuid

from api.models import Ad, User


def get_by(pk: int = None, uuid: uuid.UUID = None) -> Ad:
    """Query a user by last and first name"""

    params = {}
    if (not pk and not uuid) or (pk and uuid):
        raise ValueError("Provide pk or uuid")

    if uuid:
        params["uuid"] = str(uuid)

    if pk:
        params["pk"] = pk

    return Ad.query.filter_by(**params).one()


def update(ad: Ad, **kwargs) -> Ad:
    """Update an already saved ad"""
    ad.update(kwargs)
    return ad.save()


def create(user: User, title: str, description: str) -> Ad:
    """Create a new ad assoicated to a user"""

    return Ad(user=user, title=title, description=description).save()
