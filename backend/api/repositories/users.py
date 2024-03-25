""" Defines the User repository """
import json

import secrets
import uuid
from flask import abort, current_app
from marshmallow import RAISE, Schema, ValidationError, fields, validate
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError, NoResultFound
from typing import Union
from werkzeug.security import generate_password_hash

from api.models import User
from api.models.status_type import StatusType
from api.models.utils import add_error, get_value
from api.repositories import users


class UserCreateSchema(Schema):
    account_id = fields.Int(required=True, metadata={"error": "Invalid account id"})
    email = fields.Str(
        required=True,
        validate=validate.Email(error="email-invalid"),
        error_messages={
            "required": "email-required",
            "invalid": "email-invalid-type",
            "type": "email-invalid-must-be-string",
        },
    )


def get_by(
    pk: int = None, uuid: uuid.UUID = None, email: str = None
) -> Union[User, None]:
    """Query a user by uuid or id"""

    params = {}
    # if (not pk and not uuid and not email) or (pk and uuid and email):
    #     raise ValueError("Provide pk, uuid or email")

    if uuid:
        params["uuid"] = str(uuid)

    if pk:
        params["pk"] = pk

    if email:
        params["email"] = email

    current_app.logger.debug(
        {"FUNCTION-CALL": "users.get_by()", "params": params, "email": email}
    )

    if bool(params):
        return User.query.filter_by(**params).one()

    return None


# @TODO FIX update method - It is not working as expected
# def update(user: User, **kwargs) -> User:
#     """Update user"""
#     user.update(kwargs)
#     return user.save()


def exists(data, errors) -> bool:
    email = get_value(data, "email", "").lower()

    found = False
    try:
        user = users.get_by(email=email)
        if user is not None:
            add_error(errors, "user", "Email already exists")
            found = True
    except ValueError as err:
        add_error(errors, "user", err.args[0])
        pass
    except NoResultFound:
        pass

    return found


def create(data: dict, errors: list) -> Union[User, None]:
    """
    Create a new user
    """
    # Instantiate the schema
    schema = UserCreateSchema()

    # Validate data
    try:
        # schema.load(data=data, partial=False, unknown=RAISE)
        schema.load(data=data)
    except ValidationError as err:
        # Parse exceptions like marshmallow.exceptions.ValidationError: {'email': ['email-required']}
        for field, messages in err.messages.items():
            for message in messages:
                add_error(errors, field, message)
        return None

    account_id = get_value(data, "account_id")

    if not account_id:
        add_error(
            errors,
            "account_id",
            "Account id is undefined. Cannot proceed with user creation",
        )
        return None

    payload = {
        "status_id": StatusType.NEW.value,
        "account_id": account_id,
        "email": get_value(data, "email"),
        # password is 16 bytes random -> 32 chars in hex
        "password_hash": generate_password_hash(secrets.token_hex(16)),
    }

    user = User(**payload)

    try:
        # refresh to get details after save
        user = user.save(refresh=True)
    except (IntegrityError, PyMySQLIntegrityError) as err:
        # "A user with this email already exists. Please use a different email."
        add_error(errors, "email", str(err))
    # Catch all exceptions and don't report because we don't want to log password_hash that is generated
    except Exception as e:
        user = None
        add_error(errors, "email", "Unknown exception")

    return user
