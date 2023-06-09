"""Auth restful resources"""
import os

import time
from flask import Flask, current_app, request, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Api, Resource, reqparse

from api.resources.base_resource import BaseResource

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)
api = Api(app)


class AuthCredentialResource(BaseResource):
    """Auth credential"""

    def post(self):
        """User Registration (new account, user and store)"""
        current_app.logger.info({"FUNCTION-CALL": "AuthCredentialResource.post"})

        resource_parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        # Add arguments
        resource_parser.add_argument(
            "username",
            type=str,
            help="Username is required",
            required=True,
            location="json",
        )
        resource_parser.add_argument(
            "password",
            type=str,
            help="Password required",
            required=True,
            location="json",
        )

        errors = self.execute_parse_args(resource_parser)

        if errors:
            return self.validate_payload(errors), 400

        json_data = request.get_json()

        username = self.v(json_data, "username")
        password = self.v(json_data, "password")

        # @TODO Login and get user details

        access_token = create_access_token(identity=username)
        return {"token": access_token}, 200

    def validate_payload(self, data):
        """Validate payload fields"""
        result = []
        errors = data["message"]

        if self.v(errors, "account_name"):
            result.append(
                {
                    "ref": "username",
                    "key": "username_is_required",
                    "message": "Username is required",
                }
            )

        if self.v(errors, "password"):
            result.append(
                {
                    "ref": "password",
                    "key": "password_is_required",
                    "message": "Password is required",
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

        # @TODO Login with username and password

        custom_response = {"success": False, "errors": result}
        return custom_response


class AuthRefreshResource(Resource):
    """Auth refresh"""

    @jwt_required()
    def get(self):
        """Refresh JWT token"""
        return {"action": url_for("auth.refresh")}, 200


class AuthCurrentResource(Resource):
    """Auth current"""

    @jwt_required()
    def get(self):
        """Get the current credential details"""
        return {"action": url_for("auth.current")}, 200


class AuthDetailsResource(Resource):
    """Auth details"""

    @jwt_required()
    def get(self):
        """Details about the current authentication (shows user roles)"""
        return {"action": url_for("auth.details")}, 200


class AuthLogoutResource(Resource):
    """Auth logout"""

    @jwt_required()
    def get(self):
        """Expire current credential"""
        return {"action": url_for("auth.logout")}, 200


class AuthTimeResource(Resource):
    """Auth time"""

    @jwt_required()
    def get(self):
        """Get the current time of the server, since UNIX epoch"""
        return {"action": url_for("auth.authtimeresource"), "time": time.time()}, 200
