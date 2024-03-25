"""Verifications Restful resources"""

from flask_restful import reqparse

from api.models import Verification
from api.models.utils import get_value
from api.repositories import verifications
from api.resources.base_resource import BaseResource

list_resource_parser = reqparse.RequestParser()
list_resource_parser.add_argument(
    "page", type=int, default=1, help="Current page", required=False, location="args"
)
list_resource_parser.add_argument(
    "size",
    type=int,
    default=20,
    help="Number of records per page",
    required=False,
    location="args",
)


class VerificationsUserResource(BaseResource):
    """Verification of User: To verify user account after registration. The token is sent by email"""

    # NOTE: This is a public endpoint
    def get(self, user_id=None, token=None):
        """This GET makes changes to table verifications e.g. is not idempotent"""
        response = {}
        http_status_code = 400
        errors = []

        data = {
            "user_id": user_id,
            "token": token,
            "type": "user",
        }

        verification_result = verifications.verify(data, errors)

        if isinstance(verification_result, Verification):
            http_status_code = 200
            response = {"id": get_value(verification_result, "id")}
            if get_value(verification_result, "date_created"):
                response["date_created_utc"] = get_value(
                    verification_result, "date_created"
                ).strftime("%Y-%m-%d %H:%M:%S")

        if errors:
            response["errors"] = errors
            http_status_code = 400

        return response, http_status_code


class VerificationsEmailResource(BaseResource):
    """Verification of Email: To verify one email that has been changed"""

    # NOTE: This is a public endpoint
    def get(self, category=None):
        """This GET makes changes to table verifications e.g. is not idempotent"""
        return None


class VerificationsOptResource(BaseResource):
    """Verification of OTP: To verify user by OTP (one time password). e.g. The token expires after 5 minutes"""

    # NOTE: This is a public endpoint
    def get(self, category=None):
        """This GET makes changes to table verifications e.g. is not idempotent"""
        return None
