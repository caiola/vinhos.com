""" Defines the User repository """
import secrets
import uuid
from typing import Any, Union

from flask import current_app
from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate, RAISE
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError, NoResultFound
from werkzeug.security import generate_password_hash

from api.models import User
from api.models.status_type import StatusType
from api.models.tools import utils
from api.repositories import users


class UserCreateSchema(Schema):
    account_id = fields.Int(required=True, error="Invalid account id")
    email = fields.Str(
        required=True,
        validate=validate.Email(error="email-invalid"),
        error_messages={
            "required": "email-required",
            "invalid": "email-invalid-type",
            "type": "email-invalid-must-be-string",
        },
    )


def get_by(pk: int = None, uuid: uuid.UUID = None, email: str = None) -> Union[User, None]:
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

    current_app.logger.debug({
        "FUNCTION-CALL": "users.get_by()",
        "params": params,
        "email": email
    })

    if bool(params):
        return User.query.filter_by(**params).one()

    return None


def update(user: User, **kwargs) -> User:
    """Update a user's age"""
    user.update(kwargs)
    return user.save()


def exists(data, errors) -> Any:
    email = utils().get_value(data, "email", "").lower()

    found = False
    try:
        user = users.get_by(email=email)
        if user is not None:
            utils().add_error(errors, "user", "Email already exists")
        found = True
    except ValueError as err:
        utils().add_error(errors, "user", err.args[0])
        pass
    except NoResultFound:
        pass

    return found


def create(data: dict) -> Union[User, None]:
    """
    Create a new user
    """
    response = {}

    # Instantiate the schema
    schema = UserCreateSchema(unknown=EXCLUDE)

    # Validate data
    result = None
    try:
        result = schema.load(data=data, partial=False, unknown=RAISE)
        user_errors = []
    except ValidationError as err:
        user_errors = [
            {"ref": ref, "message": msg}
            for ref, msgs in err.messages.items()
            for msg in msgs
        ]

    account_id = utils().get_value(data, "account_id")

    if not account_id:
        user_errors.append(
            {"ref": "user.account_id", "message": "Account id is undefined. Cannot proceed with user creation"})
    else:
        payload = {
            "status_id": StatusType.NEW.value,
            "account_id": account_id,
            "email": utils().get_value(data, "email"),
            # password is 16 bytes random -> 32 chars in hex
            "password_hash": generate_password_hash(secrets.token_hex(16)),
        }

        user = User(**payload)

        # Catch all exceptions because we dont want to log password_hash that is generated
        try:
            # refresh to get details after save
            user = user.save(refresh=True)
        except (IntegrityError, PyMySQLIntegrityError) as err:
            user = None
            user_errors.append(
                {
                    "ref": "email",
                    # "message": "A user with this email already exists. Please use a different email.",
                    "message": str(err)
                }
            )
        except Exception as e:
            user = None
            user_errors.append({"ref": "email", "message": "Unknown exception"})

        if user:
            response["user_id"] = user.id

    if user_errors:
        response["errors"] = user_errors

    return response
