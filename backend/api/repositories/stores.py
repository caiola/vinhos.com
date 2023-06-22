""" Defines the Store repository """
from marshmallow import EXCLUDE, RAISE, Schema, ValidationError, fields
from pymysql.err import IntegrityError as PyMySQLIntegrityError
from sqlalchemy.exc import IntegrityError, NoResultFound
from typing import Any, Union

from api.models import Store
from api.models.status_type import StatusType
from api.models.utils import add_error, get_value
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


def exists(data, errors) -> Any:
    # @TODO Check if there is at least one store
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


def create(data: dict, errors: list) -> Union[Store, None]:
    """
    Create a new store
    """

    store = None

    data_validation = {
        "account_id": data["account_id"],
        "store_name": data["store_name"],
    }

    # Instantiate the schema
    schema = StoreCreateSchema(unknown=EXCLUDE)

    # Validate data
    try:
        schema.load(data=data_validation, partial=False, unknown=RAISE)
    except ValidationError as err:
        errors.append(
            [
                {"ref": ref, "message": msg}
                for ref, msgs in err.messages.items()
                for msg in msgs
            ]
        )

    account_id = get_value(data, "account_id")

    if not account_id:
        errors.append(
            {
                "ref": "store.account_id",
                "message": "Account id is undefined. Cannot proceed with user creation",
            }
        )
        return store

    payload = {
        "status_id": StatusType.NEW.value,
        "account_id": data["account_id"],
        "store_name": data["store_name"],
    }

    store = Store(**payload)

    # Catch all exceptions because we dont want to log password_hash that is generated
    try:
        # refresh to get details after save
        store = store.save(refresh=True)
    except (IntegrityError, PyMySQLIntegrityError) as err:
        errors.append(
            {
                "ref": "email",
                # "message": "A user with this email already exists. Please use a different email.",
                "message": str(err),
            }
        )
    except Exception as e:
        errors.append({"ref": "email", "message": "Unknown exception"})

    return store
