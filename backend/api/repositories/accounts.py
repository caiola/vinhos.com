""" Defines the Account repository """
import random
from itertools import count

from flask import abort

from api.models import Account
from api.models.countries import Countries
from api.models.status_type import StatusType
# from marshmallow import validate, ValidationError
from marshmallow import Schema, fields, validate, ValidationError, schema


class AccountCreateSchema(Schema):
    # email = fields.Str(required=True, validate=validate.Email(error='invalid-email'))
    email = fields.Str(required=True,
                       validate=validate.Email(error="email-invalid"),
                       error_messages={"required": "email-required",
                                       "invalid": "invalid-email",
                                       "type": "invalid-email-invalid-must-be-string"})


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


def create(account_info: dict) -> Account:
    """Create a new account"""

    # id = db.Column(db.BigInteger(), primary_key=True, nullable=False)
    # status_id = db.Column(db.Integer(), default=StatusType.NEW, nullable=False, comment="Status id")
    # address_id = db.Column(db.BigInteger(), nullable=True, comment="Address id")
    # account_name = db.Column(db.String(60), nullable=True, comment="Account can have any name, it is an internal reference")
    # country = db.Column(db.String(2), nullable=True)
    # company_name = db.Column(db.String(50), nullable=True)
    # tax_number = db.Column(db.String(50), nullable=True)

    data = {"email": account_info["email"]}

    # Instantiate the schema
    schema = AccountCreateSchema()

    # Validate an email
    try:
        result = schema.load(data)
    except ValidationError as err:
        result = None
        print(err.messages)  # Will print: {'email': ['Invalid email.']}
        raise ValueError(str(err))

    # abort(vars(result), 400)

    # validator = validate.And(validate.Email(error=  "Email is not valid"))
    # validator = validate.Email(email, error="Email is not valid")
    # result = validator(email)

    # if count(result) > 0:
    #     raise ValueError(result)

    data = {
        "status_id": StatusType.NEW.value,
        "address_id": None,
        "account_name": "account-" + str(random.randint(100000, 10000000)),
        # @TODO User can change country later
        "country": Countries.PT.name
    }

    account = Account(**data)
    # store = Account(account_name=account_name, company_name=company_name)
    # user = Account(account_name=account_name, company_name=company_name)

    return account.save()
