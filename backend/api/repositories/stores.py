""" Defines the Store repository """

from flask import abort
from marshmallow import Schema, fields, ValidationError, EXCLUDE
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError

from api.models import Store
from api.models.status_type import StatusType


class StoreCreateSchema(Schema):
    account_id = fields.Int(required=True)
    store_name = fields.Str(required=True)


def get_by(pk: int = None, name: str = None) -> Store:
    """Query a store by uuid or id"""

    params = {}
    if (not pk and not name) or (pk and name):
        raise ValueError("Provide pk or name")

    if name:
        params["name"] = str(name)

    if pk:
        params["pk"] = pk

    return Store.query.filter_by(**params).one()


def update(store: Store, **kwargs) -> Store:
    """Update store"""
    store.update(kwargs)
    return store.save()


def create(data: dict) -> Store:
    """
    Create a new store
    """

    data_validation = {
        "status_id": StatusType.NEW.value,
        "account_id": data["account_id"],
        "store_name": data["store_name"]
    }

    # Instantiate the schema
    schema = StoreCreateSchema(unknown=EXCLUDE)

    # Validate data
    try:
        result = schema.load(data_validation)
    except ValidationError as err:
        abort(400, err.messages)

    payload = {
        "status_id": StatusType.NEW.value,
        "account_id": data["account_id"],
        "store_name": data["store_name"]
    }

    store = Store(**payload)

    store_result = store.save(refresh=True)
    #
    # try:
    #     # refresh to get details after save
    #     store_result = store.save(refresh=True)
    # except (IntegrityError, PyMySQLIntegrityError) as e:
    #     store_result = None
    #     abort(400, _("A store with the same criteria already exists."))
    # except Exception as e:
    #     store_result = None
    #     abort(400, _("Unknown exception"))

    return store_result
