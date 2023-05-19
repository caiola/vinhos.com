"""Ads Restful resources"""
import json

from flask_jwt_extended import JWTManager, create_access_token
from flask import url_for, current_app, request
from flask_restful import Resource, abort, marshal_with, reqparse

from api.repositories import ads, accounts

from .serializers import AdSerializer, ListSerializer, AccountSerializer


ads_resource_parser = reqparse.RequestParser()
ads_resource_parser.add_argument(
    "page", type=int, default=1, help="Current page", required=False, location="args"
)
ads_resource_parser.add_argument(
    "size",
    type=int,
    default=10,
    help="Number of records per page",
    required=False,
    location="args",
)


class AdsResource(Resource):
    """Cursors through ads"""

    @marshal_with(ListSerializer)
    def get(self):
        args = ads_resource_parser.parse_args()
        pagination = ads.list().paginate(page=args["page"], per_page=args["size"])

        return {
            "total": pagination.total,
            "previous": url_for(
                "ads.adsresource", page=args["page"] - 1, size=args["size"]
            )
            if pagination.has_prev
            else None,
            "next": url_for("ads.adsresource", page=args["page"] + 1, size=args["size"])
            if pagination.has_next
            else None,
            "results": pagination.items,
        }

    def post(self):
        """Creates a resource"""
        args = ads_resource_parser.parse_args()
        pagination = ads.list().paginate(page=args["page"], per_page=args["size"])


class AdResource(Resource):
    """Retrieves an add"""

    @marshal_with(AdSerializer)
    def get(self, pk: str):
        """Retrieves a given resource"""

        instance = ads.get_by(uuid=pk)
        if not instance:
            abort(404)
        return instance


class AccountResource(Resource):
    """Manage account resources"""

    @marshal_with(AccountSerializer)
    def post(self):
        """Create account resource"""

        account_resource_parser = reqparse.RequestParser()
        account_resource_parser.add_argument(
            "account_name", type=int, default=1, help="Account name", required=False, location="args"
        )

        args = account_resource_parser.parse_args()

        return {"account": "Account created successfully"}, 201


class CustomRequestParser(reqparse.RequestParser):
    def parse_args(self, req=None, strict=False, http_error_code=400, bundle_errors=False):
        try:
            return super().parse_args(req, strict, http_error_code, bundle_errors)
        except Exception as e:
            current_app.logger.debug({"DVL-FUNCTION": "§LoginResource §CustomRequestParser"})

            json_data = request.get_json()
            current_app.logger.debug({"json.data": json.dumps(json_data)})

            validation_errors = LoginResource().validate_login_fields(json_data)

            if validation_errors:
                custom_response = {"success": False, "errors": validation_errors}
                abort(400, **custom_response)


class LoginResource(Resource):
    """Login management"""

    def post(self):
        """Retrieves a given resource"""

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

        # @TODO is getting json from payload twice
        json_data = request.get_json()

        username = json_data["username"]

        # @TODO Login with username and password

        access_token = create_access_token(identity=username)
        return {"token": access_token}, 200

    def validate_login_fields(self, data):
        """Validate the username and password fields"""

        errors = []

        # Perform validation checks
        if "username" not in data or not data["username"]:
            errors.append({"field": "username", "key": "username_is_required", "message": "Username is required"})

        if "password" not in data or not data["password"]:
            errors.append({"field": "password", "key": "password_is_required", "message": "Password is required"})

        return errors
