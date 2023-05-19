"""Account Restful resources"""
from flask import current_app, abort, request
from flask_restful import Resource, reqparse

from api.resources.auth import AuthCredentialResource


class CustomRequestParser(reqparse.RequestParser):
    def parse_args(self, req=None, strict=False, http_error_code=400, bundle_errors=False):
        try:
            return super().parse_args(req=req, strict=strict, http_error_code=http_error_code)
        except Exception as e:
            current_app.logger.info({"DVL-FUNCTION": "§AccountResource §CustomRequestParser"})

            return False
            # try:
            #     json_data = request.get_json()
            # except Exception as e:
            #     json_data = {}
            #     custom_response = {"success": False,
            #                        "errors": [
            #                            {"ref": "payload", "key": "invalid_payload", "message": "Invalid payload"}]}
            #     # return {"account": "abcaaa"}, 201
            #     abort(400, **custom_response)

            # validation_errors = AccountResource().validate_login_fields(json_data)
            #
            # if validation_errors:
            #     custom_response = {"success": False, "errors": validation_errors}
            #     abort(400, **custom_response)


class AccountResource(Resource):
    """Account management"""

    def v(self, json_data, key):
        try:
            return json_data[key]
        except KeyError:
            return None

    def post(self):
        """User Registration (new account, user and store)"""

        # Setup parser with custom response
        resource_parser = CustomRequestParser(trim=True, bundle_errors=True)

        # Add arguments
        resource_parser.add_argument(
            "company_name", type=str, help="Company name", required=True, location="json"
        )
        # resource_parser.add_argument(
        #     "password", type=str, help="Password", required=True, location="json"
        # )

        args = resource_parser.parse_args()

        current_app.logger.debug({"PAYLOAD_JSON": args})

        # try:
        #     json_data = request.get_json()
        # except Exception as e:
        #     json_data = []
        #     custom_response = {"success": False,
        #                        "errors": [
        #                            {"ref": "payload", "key": "invalid_payload", "message": "Invalid payload"}]}
        #     abort(400, **custom_response)

        # company_name = self.v(json_data, "company_name")
        # password = self.v(json_data, "password")

        # @TODO Login with username and password

        return {"account": "abc"}, 201


def validate_login_fields(self, data):
    """Validate ields"""

    errors = []

    # Perform validation checks
    if "company_name" not in data or not data["company_name"]:
        errors.append({"ref": "company_name", "key": "company_is_required", "message": "Company name is required"})

    # if "password" not in data or not data["password"]:
    #     errors.append({"ref": "password", "key": "password_is_required", "message": "Password is required"})
    #
    return errors
