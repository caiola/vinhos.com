""" Defines the Account repository """
import random
from itertools import count

from flask import abort

from api.models import Account, User
from api.models.countries import Countries
from api.models.status_type import StatusType
# from marshmallow import validate, ValidationError
from marshmallow import Schema, fields, validate, ValidationError, schema, EXCLUDE

from api.repositories import users
from api.repositories.users import UserCreateSchema


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
    ###########################################################################
    Create a new account
    ###########################################################################
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
    # store = Account(account_name=account_name, company_name=company_name)
    # user = Account(account_name=account_name, company_name=company_name)

    #return 'Last inserted id: ' + str(account.id)

    #return account.save()
    # return account_result = account.save()

    # """
    # Example of account_result:
    # {
    #     "msg": "account-created",
    #     "data": {
    #         "email": "robccsilva@gmail.com"
    #     }
    # }
    # """

    ############################################################################
    # Create a new store
    ############################################################################
    print("create store...")

    ############################################################################
    # Create a new user
    ############################################################################
    print("create user...")
    payload = {
        # "status_id": StatusType.NEW.value,
        "account_id": account.id,
        "email": data["email"]
    }
    # user = User(**payload)
    # user.create()
    user_result = users.create(payload)

    return user_result
