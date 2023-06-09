"""Stores Restful resources"""

from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from api.resources.base_resource import BaseResource


class StoresResource(BaseResource):
    """Stores management"""

    @jwt_required()
    def post(self):
        """Create store"""

        resource_parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        # Add arguments
        resource_parser.add_argument(
            "store_name",
            type=str,
            help="Store name is required",
            required=True,
            location="json",
        )

        errors = self.execute_parse_args(resource_parser)

        if errors:
            return self.validate_payload(errors), 400

        # @TODO User Registration (new account, user and store)

        custom_response = {"msg": "account-created"}
        return custom_response, 418

    def validate_payload(self, data):
        """Validate payload fields"""
        result = []
        errors = data["message"]

        if self.v(errors, "store_name"):
            result.append(
                {
                    "ref": "store_name",
                    "key": "store_name_is_required",
                    "message": "Store name is required",
                }
            )

        if self.v(errors, "payload"):
            result.append(
                {
                    "ref": "payload",
                    "key": "payload_invalid",
                    "message": "Payload is invalid",
                }
            )

        if self.v(errors, "unknown"):
            result.append(
                {
                    "ref": "unknown",
                    "key": "unknown_exception",
                    "message": self.v(errors, "unknown"),
                }
            )

        custom_response = {"success": False, "errors": result}
        return custom_response
