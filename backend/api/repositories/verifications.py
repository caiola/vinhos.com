""" Defines the Verification repository """

import uuid
from typing import Union

import pytz
from marshmallow import Schema, ValidationError, fields
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError

from api.models import User, Verification
from api.models.utils import add_error, get_value


class VerificationCreateSchema(Schema):
    user_id = fields.Int(required=True, error="Invalid user id")


# def exists(data, errors) -> bool:
#     email = get_value(data, "email", "").lower()
#
#     found = False
#     try:
#         user = users.get_by(email=email)
#         if user is not None:
#             add_error(errors, "user", "Email already exists")
#             found = True
#     except ValueError as err:
#         add_error(errors, "user", err.args[0])
#         pass
#     except NoResultFound:
#         pass
#
#     return found


def create(data: dict, errors: list) -> Union[User, None]:
    """
    Create a new verification
    """
    # Instantiate the schema
    schema = VerificationCreateSchema()

    # Validate data
    try:
        schema.load(data=data)
    except ValidationError as err:
        for field, messages in err.messages.items():
            for message in messages:
                add_error(errors, field, message)
        return None

    payload = {
        "user_id": get_value(data, "user_id"),
        "action": "registration",
        "token": uuid.uuid4(),
        "date_created": pytz.timezone('UTC')
    }

    verification = Verification(**payload)

    try:
        # refresh to get details after save
        verification = verification.save(refresh=True)
    except (IntegrityError, PyMySQLIntegrityError) as err:
        # "Verification for this kind already exists"
        verification = None
        add_error(errors, "verification", str(err))
    # Catch all exceptions and don't report because we don't want to log password_hash that is generated
    except Exception as e:
        verification = None
        add_error(errors, "verification", "Unknown exception")

    return verification
