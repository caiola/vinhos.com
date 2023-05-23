"""Accounts Restful resources"""
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from api.repositories import accounts
from api.resources.base_resource import BaseResource


class AccountsResource(BaseResource):
    """Accounts management"""

    @jwt_required()
    def post(self):
        """User Registration (new account, user and store)"""

        resource_parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        # Add arguments
        # resource_parser.add_argument(
        #     "company_name", type=str, help="Company name is required", required=True, location="json"
        # )
        resource_parser.add_argument(
            "email", type=str, help="Email is required", required=True, location="json"
        )

        errors = self.execute_parse_args(resource_parser)

        if errors:
            return self.validate_payload(errors), 400

        data = request.get_json()

        accounts.create(data)

        # Do not send password_hash
        data.pop("password_hash", None)

        custom_response = {"msg": "account-created", "data": data}
        return custom_response, 418

    def validate_payload(self, data):
        """Validate payload fields"""
        result = []
        errors = data["message"]

        if self.v(errors, "email"):
            result.append({"ref": "email", "key": "email_is_required", "message": "Email is required"})

        if self.v(errors, "payload"):
            result.append(
                {"ref": "payload", "key": "payload_invalid", "message": "Payload is invalid"})

        if self.v(errors, "unknown"):
            result.append(
                {"ref": "unknown", "key": "unknown_exception", "message": self.v(errors, "unknown")})

        custom_response = {"success": False, "errors": result}
        return custom_response
