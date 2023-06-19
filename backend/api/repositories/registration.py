""" Defines the Account, User, Store registration repository """
import json

from flask import current_app

from api import db
from api.models.utils import get_value
from api.repositories import accounts, stores, users, verifications


def registration(data: dict):
    response = {}

    current_app.logger.debug({"FUNCTION-CALL": "accounts.registration()", "data": data})

    # Check prerequisites: account name and email must be unique
    errors = []

    accounts.exists(data, errors)
    users.exists(data, errors)

    current_app.logger.debug(
        {"FUNCTION-CALL": "accounts.registration().exists", "errors": errors}
    )

    # If errors are found return to client
    if bool(errors):
        return {"errors": errors}

    # Create a new account
    payload = {
        "country": get_value(data=data, key="country"),
        "account_name": get_value(data=data, key="account_name"),
    }
    account_result = accounts.create(payload, errors)

    account_id = get_value(data=account_result, key="id")

    # Create a new user
    payload = {
        "account_id": account_id,
        "email": get_value(data=data, key="email"),
    }

    current_app.logger.debug(
        {
            "FUNCTION-CALL": "accounts.registration().user-payload",
            "payload": payload,
            "type": type(account_result),
            "errors": errors,
        }
    )

    user_result = users.create(payload, errors)

    user_id = get_value(data=user_result, key="id")

    current_app.logger.debug(
        {
            "FUNCTION-CALL": "accounts.registration().user_result",
            "user_id": user_id,
            "type": type(user_result),
        }
    )

    # Create a new store
    payload = {
        "account_id": account_id,
        "store_name": get_value(data=data, key="account_name"),
    }

    current_app.logger.debug(
        {"FUNCTION-CALL": "accounts.registration().store-payload", "payload": payload}
    )

    store_result = stores.create(payload, errors)
    store_id = get_value(data=store_result, key="id")

    # Set the user as administrator on the account
    # Commit the changes to the database session
    try:
        db.session.add(account_result)
        account_result.user_id = user_result.id
        db.session.commit()
    finally:
        db.session.close()

    # @TODO Refactor to update() method, not sure why but BaseModel/abc.py is not working properly
    # account_result.update(payload)

    # Create a new verification
    payload = {
        "user_id": user_id,
    }

    verification_result = verifications.create(payload, errors)
    verification_id = get_value(data=verification_result, key="id")

    current_app.logger.debug(
        {"FUNCTION-CALL": "accounts.registration().verification_id", "verification_id": verification_id}
    )

    # Merge response with account, user, store
    response = {
        "account_id": account_id,
        "user_id": user_id,
        "store_id": store_id,
    }

    if errors:
        response = {**response, **{"errors": errors}}

    return response
