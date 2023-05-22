""" Defines the User repository """
import uuid

from werkzeug.security import generate_password_hash

from api.models import User
from sqlalchemy.orm import Session

from api.models.status_type import StatusType


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


# def create(first_name: str, last_name: str) -> User:
def create(user_info: dict) -> User:
    """Create a new user"""
    # You would normally get session from your SQLAlchemy DB instance, e.g., db.session if using Flask-SQLAlchemy

    data = {
        "status_id": StatusType.NEW.value,
        "first_name": user_info.get("first_name"),
        "middle_name": user_info.get("middle_name"),
        "last_name": user_info.get("last_name"),
        # "email": user_info.get("email")
        "password_hash": generate_password_hash("default.password")
    }

    user = User(**data)
    return user.save()

    # @TODO Evaluate if it is better to to have code like below, to rollback on errors
    # user = User()
    # user.status_id = StatusType.NEW.value
    # user.first_name = user_info["first_name"]
    # user.middle_name = user_info["middle_name"]
    # user.last_name = user_info["last_name"]
    # user.email = user_info["email"]
    #
    # user.create(user_info)

    # session = Session()
    # try:
    #     session.add(user)
    #     session.commit()
    #     session.refresh(user)
    # except:
    #     session.rollback()
    #     raise
    # finally:
    #     session.close()
    #
    # return user
