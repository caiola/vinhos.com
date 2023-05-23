""" Defines the Account repository """
import random

from marshmallow import Schema, fields, validate, ValidationError

from api.models import Account
from api.models.countries import Countries
from api.models.status_type import StatusType
from api.models.tools import utils
from api.repositories import accounts, stores
from api.repositories import users


class AccountCreateSchema(Schema):
    email = fields.Str(required=True,
                       validate=validate.Email(error="Invalid email"),
                       error_messages={"required": "Email required",
                                       "invalid": "Invalid type",
                                       "type": "Email must be string"})


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


def registration(data: dict):
    response = {}

    # ############################################################################
    # Create a new account
    # ############################################################################
    payload = {
        "email": utils.v(data, "email")
    }
    account_result = accounts.create(payload)

    response["account"] = account_result

    # ############################################################################
    # Create a new store
    # ############################################################################

    payload = {
        "account_id": utils.v(account_result, "account_id"),
        "store_name": "store-" + str(random.randint(100000, 10000000)),
    }

    store_result = stores.create(payload)

    response["store"] = store_result

    # ############################################################################
    # Create a new user
    # ############################################################################

    payload = {
        "account_id": utils.v(account_result, "account_id"),
        "email": data["email"]
    }

    user_result = users.create(payload)

    response["user"] = user_result

    return response


def create(data: dict) -> Account:
    """
    Create a new account, user and store
    """

    # Instantiate the schema
    schema = AccountCreateSchema()

    account_errors = None

    # Validate payload
    try:
        result = schema.load(data)
    except ValidationError as err:
        account_errors = [{"ref": ref, "message": msg} for ref, msgs in err.messages.items() for
                          msg in msgs]

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

    response = {}
    response["account_id"] = account_id
    response["account_errors"] = account_errors

    return response
