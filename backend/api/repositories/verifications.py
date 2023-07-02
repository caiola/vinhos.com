""" Defines the Verification repository """

import uuid
from flask import current_app
from marshmallow import Schema, ValidationError, fields, validate
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError, NoResultFound
from typing import Optional, Union

from api.models import Verification
from api.models.utils import add_error, get_value


class VerificationCreateSchema(Schema):
    user_id = fields.Int(required=True, metadata={"error": "Invalid user id"})
    type = fields.Str(required=True, metadata={"error": "Invalid verification type"})


class VerificationUserSchema(Schema):
    user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1),
        metadata={"error": "Invalid user id"},
    )
    token = fields.Str(required=True, metadata={"error": "Invalid token"})
    type = fields.Str(required=True, metadata={"error": "Invalid verification type"})


def get_by(
    user_id: int = None, token: str = None, verification_type: str = None
) -> Union[Verification, None]:
    """Query to get token verification"""

    params = {}
    if not user_id or not token or not verification_type:
        raise ValueError("Provide user id, token and verification type")

    if user_id:
        params["user_id"] = user_id

    if token:
        params["token"] = token

    if verification_type:
        params["type"] = verification_type

    current_app.logger.debug(
        {"FUNCTION-CALL": "verifications.get_by()", "params": params}
    )

    if bool(params):
        return Verification.query.filter_by(**params).one()

    return None


def create(data: dict, errors: list) -> Union[Verification, None]:
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
        "type": get_value(data, "type"),
        "token": uuid.uuid4(),
        # Field: date_created is filled at database level with default timestamp value
        # e.g. "date_created": datetime.now(pytz.utc),
    }

    verification = Verification(**payload)

    try:
        # refresh to get details after save
        verification = verification.save(refresh=True)
    except (IntegrityError, PyMySQLIntegrityError) as err:
        # "Verification for this kind already exists"
        verification = None
        add_error(errors, "verification", str(err))

    return verification


def verify(data: dict, errors: list) -> Optional[Verification]:
    """
    Verify user token
    """
    # Instantiate the schema
    schema = VerificationUserSchema()

    # Validate data
    try:
        schema.load(data=data)
    except ValidationError as err:
        for field, messages in err.messages.items():
            for message in messages:
                add_error(errors, field, message)
        return None

    current_app.logger.debug(
        {"FUNCTION-CALL": "verifications.verify()", "data": data, "errors": errors}
    )

    try:
        verification = get_by(
            user_id=get_value(data, "user_id"),
            token=get_value(data, "token"),
            verification_type=get_value(data, "type"),
        )

    except (NoResultFound) as err:
        verification = None
        add_error(errors, "verification", "Token not found")

    return verification
