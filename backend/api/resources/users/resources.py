"""Users Restful resources"""
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from api.models.status_type import StatusType
from api.models.utils import get_value
from api.repositories import users
from api.resources.base_resource import BaseResource


class UsersResource(BaseResource):
    """Users management"""

    @jwt_required()
    def post(self):
        """User Registration (new user, user and store)"""

        resource_parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        # Add arguments
        resource_parser.add_argument(
            "first_name",
            type=str,
            help="First name is required",
            required=True,
            location="json",
        )
        resource_parser.add_argument(
            "middle_name",
            type=str,
            help="Middle name is required",
            required=True,
            location="json",
        )
        resource_parser.add_argument(
            "last_name",
            type=str,
            help="Last name is required",
            required=True,
            location="json",
        )

        errors = []
        data = request.get_json()

        user_result = users.create(data, errors)

        # Do not send password_hash
        if user_result:
            user_result.pop("password_hash", None)

        if errors:
            user_result["errors"] = errors

        return user_result, 201


def validate_payload(self, data):
    """Validate payload fields"""
    result = []
    errors = data["message"]

    if get_value(errors, "first_name"):
        result.append(
            {
                "ref": "first_name",
                "key": "first_name_is_required",
                "message": "First name is required",
            }
        )

    if get_value(errors, "last_name"):
        result.append(
            {
                "ref": "last_name",
                "key": "last_is_required",
                "message": "Last name is required",
            }
        )

    if get_value(errors, "payload"):
        result.append(
            {
                "ref": "payload",
                "key": "payload_invalid",
                "message": "Payload is invalid",
            }
        )

    if get_value(errors, "unknown"):
        result.append(
            {
                "ref": "unknown",
                "key": "unknown_exception",
                "message": self.v(errors, "unknown"),
            }
        )

    custom_response = {"success": False, "errors": result}
    return custom_response
