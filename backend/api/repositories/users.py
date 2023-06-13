""" Defines the User repository """
import secrets
import uuid
from flask import abort
from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from api.models import User
from api.models.status_type import StatusType
from api.models.tools import utils


class UserCreateSchema(Schema):
    email = fields.Str(
        required=True,
        validate=validate.Email(error="email-invalid"),
        error_messages={
            "required": "email-required",
            "invalid": "email-invalid-type",
            "type": "email-invalid-must-be-string",
        },
    )


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


def create(data: dict) -> User:
    """Create a new user"""

    data_validation = {"status_id": StatusType.NEW.value, "email": data["email"]}

    # Instantiate the schema
    schema = UserCreateSchema(unknown=EXCLUDE)

    # Validate an user data
    try:
        result = schema.load(data_validation)
    except ValidationError as err:
        abort(400, err.messages)

    payload = {
        "status_id": StatusType.NEW.value,
        "account_id": data["account_id"],
        "email": data["email"],
        "first_name": None,
        "middle_name": None,
        "last_name": None,
        # password is 16 bytes random -> 32 chars in hex
        "password_hash": generate_password_hash(secrets.token_hex(16)),
    }

    user = User(**payload)

    user_errors = []

    # Catch all exceptions because we dont want to log password_hash that is generated
    try:
        # refresh to get details after save
        user_result = user.save(refresh=True)
    except (IntegrityError, PyMySQLIntegrityError) as e:
        user_result = None
        user_errors.append(
            {
                "ref": "email",
                "message": "A user with this email already exists. Please use a different email.",
            }
        )
    except Exception as e:
        user_result = None
        user_errors.append({"ref": "email", "message": "Unknown exception"})

    response = {}
    response["user_id"] = utils.v(user_result, "user_id")
    response["errors"] = user_errors

    return response
