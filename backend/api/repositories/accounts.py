""" Defines the Account repository """
import json

import pycountry
import random
from flask import abort, current_app
from marshmallow import Schema, ValidationError, fields, validate, EXCLUDE, RAISE, INCLUDE

from api.models import Account
from api.models.status_type import StatusType
from api.models.tools import utils
from api.repositories import stores, users, accounts


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

    # Create a new account
    payload = {
        "country": utils.v(data, "country"),
        "account_name": utils.v(data, "account_name"),
        "email": utils.v(data, "email")
    }
    account_result = accounts.create(payload)

    response["account"] = account_result

    return account_result

    # Create a new store

    payload = {
        "account_id": utils.v(account_result, "account_id"),
        "store_name": "store-" + str(random.randint(100000, 10000000)),
    }

    store_result = stores.create(payload)

    response["store"] = store_result

    # Create a new user

    payload = {
        "account_id": utils.v(account_result, "account_id"),
        "email": data["email"],
    }

    user_result = users.create(payload)

    response["user"] = user_result

    return response


def create(data: dict) -> Account:
    """
    Create a new account
    """

    # Instantiate the schema
    schema = AccountCreateSchema()

    # Validate an email
    result = None
    try:
        result = schema.load(data=data, partial=False, unknown=RAISE)
        account_errors = []
    except ValidationError as err:
        account_errors = [
            {"ref": ref, "message": msg}
            for ref, msgs in err.messages.items()
            for msg in msgs
        ]

    # Debug errors
    # return account_errors

    country = pycountry.countries.get(alpha_2=data.get("country").upper())
    if country is None:
        country2 = "pt"
    else:
        country2 = country.alpha_2.lower() if hasattr(country, 'alpha_2') else "pt"

    account_name = data.get("account_name").lower()

    try:
        accounts.get_by(name=account_name)
        found = True
        account_errors += [
            {"ref": "account", "message": "Account name already exists"}
        ]
    except:
        found = False

    # DEBUG :: Log country
    current_app.logger.debug({country: country2})

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

    # payload = {
    #     "account_id": account_id,
    #     "store_name": "store-" + str(random.randint(100000, 10000000)),
    # }
    #
    # store_result = stores.create(payload)
    #
    # ############################################################################
    # # Create a new user
    # ############################################################################
    # payload = {
    #     # "status_id": StatusType.NEW.value,
    #     "account_id": account_id,
    #     "email": data["email"],
    # }
    #
    # user_result = users.create(payload)
    #
    # return user_result
