"""Accounts Restful resources"""
from flask import request
from flask_jwt_extended import jwt_required

from api.repositories import registration
from api.resources.base_resource import BaseResource


class AccountsResource(BaseResource):
    """Accounts management"""

    @jwt_required()
    def post(self):
        """User Registration (new account, user and store)"""

        if request.is_json:
            data = request.get_json()
        else:
            data = None

        result = registration.registration(data)

        # Do not send password_hash
        try:
            result.pop("password_hash", None)
        except Exception as e:
            pass

        return result, 201
