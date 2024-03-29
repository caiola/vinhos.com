""" Defines the Account repository """

import pycountry
from flask import current_app
from marshmallow import RAISE, Schema, ValidationError, fields, validate
from sqlalchemy.exc import NoResultFound
from typing import Any, Union

from api.models import Account
from api.models.status_type import StatusType
from api.models.utils import add_error, get_value
from api.repositories import accounts


class AccountCreateSchema(Schema):
    country = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=2),
        metadata={"error": "Invalid country"},
    )
    account_name = fields.Str(
        required=True,
        validate=validate.Length(min=3),
        metadata={"error": "Invalid account name"},
    )
    email = fields.Str(
        required=True,
        validate=validate.Email(error="email-invalid"),
        error_messages={
            "required": "email-required",
            "invalid": "email-invalid-type",
            "type": "email-invalid-must-be-string",
        },
    )

    # @TODO Country validation not working when looking up with 2 letters country name
    # country = fields.Str(
    #     required=True,
    #     validate=validate.OneOf(
    #         [item.alpha_2.lower() for item in pycountry.countries], error="invalid-country"
    #     ),
    # )


def get_by(id: int = None, name: str = None) -> Account:
    """Query account by uuid or id"""
    params = {}
    if (not id and not name) or (id and name):
        raise ValueError("Provide id or name")

    if name:
        params["account_name"] = name

    if id:
        params["id"] = id

    return Account.query.filter_by(**params).one()


def exists(data, errors) -> Any:
    account_name = get_value(data, "account_name", "").lower()

    found = False
    try:
        account = accounts.get_by(name=account_name)
        if account is not None:
            add_error(errors, "account", "Account name already exists")
        found = True
    except NoResultFound:
        pass

    return found


def create(data: dict, errors: list) -> Union[Account, None]:
    """
    Create a new account
    """
    # Instantiate the schema
    schema = AccountCreateSchema()

    # Check for empty data
    if not data:
        add_error(errors, "account", "Data is empty.")
        return None

    # Validate data
    try:
        schema.load(data=data, partial=True, unknown=RAISE)
    except ValidationError as err:
        # Parse exceptions like marshmallow.exceptions.ValidationError: {"email": ["email-required"]}
        for field, messages in err.messages.items():
            for message in messages:
                add_error(errors, field, message)
        return None

    # print(errors)

    # Always assume "pt" (Portugal) by default, if not defined
    country = pycountry.countries.get(alpha_2=get_value(data, "country", "").upper())
    if bool(country):
        country2 = country.alpha_2.lower() if hasattr(country, "alpha_2") else "pt"
    else:
        country2 = "pt"

    account_name = get_value(data, "account_name", "").lower()

    # @TODO Refactor to use method .exists()
    try:
        account = accounts.get_by(name=account_name)
        add_error(errors, "account", "Account name already exists")
        # Return account found to work like active pattern record
        return account
    except NoResultFound as err:
        # We can proceed because the account name does not exist
        pass

    # DEBUG :: Log country
    current_app.logger.debug(
        {
            "FUNCTION-CALL": "accounts.create()",
            "country": country,
            "country2": country2,
            "errors_account_registration": errors,
            "name": account_name,
        }
    )

    response = {}

    payload = {
        "status_id": StatusType.NEW.value,
        "address_id": None,
        "account_name": data.get("account_name"),
        "country": country2,
    }

    # print(payload)

    account = Account(**payload)

    account_result = account.save(refresh=True)
    account_id = account_result.id

    response["account_id"] = account_id

    #     response["errors"] = account_errors

    return account
