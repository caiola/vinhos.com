"""Auth restful resources"""
import json
import time

from flask_jwt_extended import JWTManager, create_access_token
from flask import current_app, request, jsonify, url_for
from flask_restful import Resource, reqparse, abort
from werkzeug.exceptions import BadRequest


class CustomRequestParser(reqparse.RequestParser):
    def parse_args(self, req=None, strict=False, http_error_code=400, bundle_errors=False):
        try:
            return super(bundle_errors=bundle_errors).parse_args(req, strict, http_error_code)
        except Exception as e:
            current_app.logger.info({"DVL-FUNCTION": "§LoginResource §CustomRequestParser"})

            try:
                json_data = request.get_json()
            except Exception as e:
                custom_response = {"success": False,
                                   "errors": [
                                       {"ref": "payload", "key": "invalid_payload", "message": "Invalid payload"}]}
                abort(400, **custom_response)

            validation_errors = AuthCredentialResource().validate_login_fields(json_data)

            if validation_errors:
                custom_response = {"success": False, "errors": validation_errors}
                abort(400, **custom_response)


class AuthCredentialResource(Resource):
    """Auth credential"""

    def v(self, json_data, key):
        try:
            return json_data[key]
        except KeyError:
            return None

    def post(self):
        """Retrieves credential"""

        # Setup parser with custom response
        resource_parser = CustomRequestParser(trim=True, bundle_errors=True)

        # Add arguments
        resource_parser.add_argument(
            "username", type=str, help="User name", required=True, location="json"
        )
        resource_parser.add_argument(
            "password", type=str, help="Password", required=True, location="json"
        )

        resource_parser.parse_args()

        try:
            json_data = request.get_json()
        except Exception as e:
            json_data = []
            custom_response = {"success": False,
                               "errors": [{"ref": "payload", "key": "invalid_payload", "message": "Invalid payload"}]}
            abort(400, **custom_response)

        username = self.v(json_data, "username")
        password = self.v(json_data, "password")

        # @TODO Login with username and password

        access_token = create_access_token(identity=username)
        return {"token": access_token}, 200

    def validate_login_fields(self, data):
        """Validate the username and password fields"""

        errors = []

        # Perform validation checks
        if "username" not in data or not data["username"]:
            errors.append({"ref": "username", "key": "username_is_required", "message": "Username is required"})

        if "password" not in data or not data["password"]:
            errors.append({"ref": "password", "key": "password_is_required", "message": "Password is required"})

        return errors


class AuthRefreshResource(Resource):
    """Auth refresh"""

    def get(self):
        """Refresh JWT token"""
        return {"action": url_for("auth.refresh")}, 200


class AuthCurrentResource(Resource):
    """Auth current"""

    def get(self):
        """Get the current credential details"""
        return {"action": url_for("auth.current")}, 200


class AuthDetailsResource(Resource):
    """Auth details"""

    def get(self):
        """Details about the current authentication (shows user roles)"""
        return {"action": url_for("auth.details")}, 200


class AuthLogoutResource(Resource):
    """Auth logout"""

    def get(self):
        """Expire current credential"""
        return {"action": url_for("auth.logout")}, 200


class AuthTimeResource(Resource):
    """Auth time"""

    def get(self):
        """Get the current time of the server, since UNIX epoch"""
        return {"action": url_for("auth.authtimeresource"), "time": time.time()}, 200
