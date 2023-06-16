""" Defines the Store repository """
from typing import Union, Any

from marshmallow import EXCLUDE, Schema, ValidationError, fields, RAISE
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError, NoResultFound

from api.models import Store
from api.models.status_type import StatusType
from api.models.utils import get_value, add_error
from api.repositories import stores


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


def exists(data, errors) -> Any:
    account_id = get_value(data, "account_id", 0)

    found = False
    try:
        store = stores.get_by(id=account_id)
        if store is not None:
            add_error(errors, "account", "Store already exists")
        found = True
    except NoResultFound:
        pass

    return found


def create(data: dict) -> Union[Store, None]:
    """
    Create a new store
    """
    response = {}

    data_validation = {
        "account_id": data["account_id"],
        "store_name": data["store_name"]
    }

    # Instantiate the schema
    schema = StoreCreateSchema(unknown=EXCLUDE)

    # Validate data
    result = None
    try:
        result = schema.load(data=data_validation, partial=False, unknown=RAISE)
        store_errors = []
    except ValidationError as err:
        store_errors = [
            {"ref": ref, "message": msg}
            for ref, msgs in err.messages.items()
            for msg in msgs
        ]

    account_id = get_value(data, "account_id")

    if not account_id:
        store_errors.append(
            {"ref": "store.account_id", "message": "Account id is undefined. Cannot proceed with user creation"})
    else:
        payload = {
            "status_id": StatusType.NEW.value,
            "account_id": data["account_id"],
            "store_name": data["store_name"]
        }

        store = Store(**payload)

        # Catch all exceptions because we dont want to log password_hash that is generated
        try:
            # refresh to get details after save
            store = store.save(refresh=True)
        except (IntegrityError, PyMySQLIntegrityError) as err:
            store = None
            store_errors.append(
                {
                    "ref": "email",
                    # "message": "A user with this email already exists. Please use a different email.",
                    "message": str(err)
                }
            )
        except Exception as e:
            store = None
            store_errors.append({"ref": "email", "message": "Unknown exception"})

        if store:
            response["store_id"] = store.id

    if store_errors:
        response["errors"] = store_errors

    return response
