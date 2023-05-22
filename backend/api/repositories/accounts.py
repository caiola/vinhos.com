""" Defines the Account repository """
import random

from flask import abort
from marshmallow import Schema, fields, validate, ValidationError

from api.models import Account
from api.models.countries import Countries
from api.models.status_type import StatusType
from api.repositories import stores
from api.repositories import users


class AccountCreateSchema(Schema):
    # email = fields.Str(required=True, validate=validate.Email(error='invalid-email'))
    email = fields.Str(required=True,
                       validate=validate.Email(error="email-invalid"),
                       error_messages={"required": "email-required",
                                       "invalid": "email-invalid-type",
                                       "type": "email-invalid-must-be-string"})


def get_by(pk: int = None, name: str = None) -> Account:
    """Query a account by uuid or id"""

    params = {}
    if (not pk and not name) or (pk and name):
        raise ValueError("Provide pk or name")

    if name:
        params["name"] = str(name)

    if pk:
        params["pk"] = pk

    return Account.query.filter_by(**params).one()


def update(account: Account, **kwargs) -> Account:
    """Update account"""
    account.update(kwargs)
    return account.save()


def create(data: dict) -> Account:
    """
    Create a new account, user and store
    """

    data_validation = {"email": data["email"]}

    # Instantiate the schema
    schema = AccountCreateSchema()

    # Validate an email
    try:
        result = schema.load(data_validation)
    except ValidationError as err:
        abort(400, err.messages)

    payload = {
        "status_id": StatusType.NEW.value,
        "address_id": None,
        "account_name": "account-" + str(random.randint(100000, 10000000)),
        # User can change country later
        "country": Countries.PT.name
    }

    account = Account(**payload)

    account_result = account.save(refresh=True)
    account_id = account_result.id

    ############################################################################
    # Create a new store
    ############################################################################

    payload = {
        "account_id": account_id,
        "store_name": "store-" + str(random.randint(100000, 10000000)),
    }

    store_result = stores.create(payload)

    ############################################################################
    # Create a new user
    ############################################################################
    payload = {
        # "status_id": StatusType.NEW.value,
        "account_id": account_id,
        "email": data["email"]
    }

    user_result = users.create(payload)

    return user_result
