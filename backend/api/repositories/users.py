""" Defines the User repository """
import uuid

from marshmallow import Schema, fields, validate, ValidationError, EXCLUDE
from werkzeug.security import generate_password_hash

from api.models import User
from api.models.status_type import StatusType


class UserCreateSchema(Schema):
    email = fields.Str(required=True,
                       validate=validate.Email(error="email-invalid"),
                       error_messages={"required": "email-required",
                                       "invalid": "email-invalid-type",
                                       "type": "email-invalid-must-be-string"})

    # first_name = fields.Str(required=False, validate=validate.Length(min=2, max=50))


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
def create(data: dict) -> User:
    """Create a new user"""
    # You would normally get session from your SQLAlchemy DB instance, e.g., db.session if using Flask-SQLAlchemy

    # data = {
    #     "status_id": StatusType.NEW.value,
    #     "first_name": user_info.get("first_name"),
    #     "middle_name": user_info.get("middle_name"),
    #     "last_name": user_info.get("last_name"),
    #     # "email": user_info.get("email")
    #     "password_hash": generate_password_hash("default.password")
    # }
    #
    # user = User(**data)
    # return user.save()

    ############################################################################
    # Create a new user
    ###########################################################################
    data_validation = {
        "status_id": StatusType.NEW.value,
        "email": data["email"]
    }

    # Instantiate the schema
    schema = UserCreateSchema(unknown=EXCLUDE)

    # Validate an user data
    try:
        result = schema.load(data_validation)
    except ValidationError as err:
        abort(400, err.messages)

    payload = {
        "status_id": StatusType.NEW.value,
        "email": data["email"],
        "first_name": None,
        "middle_name": None,
        "last_name": None,
        "password_hash": generate_password_hash("default.password")
    }

    user = User(**payload)
    # store = Account(account_name=account_name, company_name=company_name)
    # user = Account(account_name=account_name, company_name=company_name)

    user_result = user.save()
