""" Defines the Ad repository """
import sqlalchemy.exc
import uuid

from api.models import Ad, User


def list():
    """Lists ads"""

    return Ad.query.order_by(Ad.id.desc())


def get_by(pk: int = None, uuid: uuid.UUID = None) -> Ad:
    """Query a user by last and first name"""

    params = {}
    if (not pk and not uuid) or (pk and uuid):
        raise ValueError("Provide pk or uuid")

    if uuid:
        params["uuid"] = str(uuid)

    if pk:
        params["pk"] = pk

    try:
        return Ad.query.filter_by(**params).one()
    except sqlalchemy.exc.NoResultFound:
        return


def update(ad: Ad, **kwargs) -> Ad:
    """Update an already saved ad"""
    ad.update(kwargs)
    return ad.save()


def create(user: User, title: str, description: str) -> Ad:
    """Create a new ad associated to a user"""

    return Ad(user=user, title=title, description=description).save()
