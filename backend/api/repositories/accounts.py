""" Defines the Account repository """
from typing import Any, Union

import pycountry
from flask import current_app
from marshmallow import Schema, fields, validate
from sqlalchemy.exc import NoResultFound

from api.models import Account
from api.models.status_type import StatusType
from api.models.utils import get_value, add_error
from api.repositories import users, accounts, stores


class AccountCreateSchema(Schema):
    country = fields.Str(required=True, error="Invalid account name")
    account_name = fields.Str(required=True, error="Invalid account name")
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


def get_by(pk: int = None, name: str = None) -> Account:
    """Query a account by uuid or id"""
    params = {}
    if (not pk and not name) or (pk and name):
        raise ValueError("Provide pk or name")

    if name:
        params["account_name"] = str(name)

    if pk:
        params["pk"] = pk

    return Account.query.filter_by(**params).one()


def update(account: Account, **kwargs) -> Account:
    """Update account"""
    account.update(kwargs)
    return account.save()


def registration(data: dict):
    response = {}

    current_app.logger.debug({
        "FUNCTION-CALL": "accounts.registration()",
        "data": data
    })

    # Check prerequisites: account name and email must be unique
    errors = []

    accounts.exists(data, errors)
    users.exists(data, errors)

    current_app.logger.debug({
        "FUNCTION-CALL": "accounts.registration().exists",
        "errors": errors
    })

    # If errors are found return to client
    if bool(errors):
        return {"errors": errors}

    # Create a new account
    payload = {
        "country": get_value(data=data, key="country"),
        "account_name": get_value(data=data, key="account_name")
    }
    account_result = accounts.create(payload)

    # Create a new user
    payload = {
        "account_id": get_value(data=account_result, key="account_id"),
        "email": get_value(data=data, key="email")
    }

    current_app.logger.debug({
        "FUNCTION-CALL": "accounts.registration().user-payload",
        "payload": payload
    })

    user_result = users.create(payload)

    # Create a new store
    payload = {
        "account_id": get_value(data=account_result, key="account_id"),
        "store_name": get_value(data=data, key="account_name")
    }

    current_app.logger.debug({
        "FUNCTION-CALL": "accounts.registration().store-payload",
        "payload": payload
    })

    store_result = stores.create(payload)

    response = {**account_result, **user_result, **store_result}

    if errors:
        response = {**response, **{"errors": errors}}

    return response


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


def create(data: dict) -> Union[Account, dict, list, None]:
    """
    Create a new account
    """

    # Instantiate the schema
    schema = AccountCreateSchema()

    country = pycountry.countries.get(alpha_2=data.get("country").upper())
    if country is None:
        country2 = "pt"
    else:
        country2 = country.alpha_2.lower() if hasattr(country, 'alpha_2') else "pt"

    account_name = data.get("account_name").lower()

    account_errors = []

    # @TODO Refactor to use method .exists()
    try:
        accounts.get_by(name=account_name)
        found = True
        add_error(account_errors, "account", "Account name already exists")
    except NoResultFound as err:
        found = False

    # DEBUG :: Log country
    current_app.logger.debug({
        "FUNCTION-CALL": "accounts.create()",
        "country": country,
        "country2": country2,
        "errors_account_registration": account_errors,
        "name": account_name,
        "found": found
    })

    response = {}

    if not found:
        payload = {
            "status_id": StatusType.NEW.value,
            "address_id": None,
            "account_name": data.get("account_name"),
            "country": country2
        }

        account = Account(**payload)

        account_result = account.save(refresh=True)
        account_id = account_result.id

        response["account_id"] = account_id

    if account_errors:
        response["errors"] = account_errors

    return response
