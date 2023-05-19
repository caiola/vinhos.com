"""Auth Restful resources"""
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError, DecodeError

from api.resources.auth.resources import AuthCredentialResource, AuthRefreshResource, AuthCurrentResource, \
    AuthDetailsResource, AuthLogoutResource, AuthTimeResource

blueprint = Blueprint("auth", __name__)
api = Api(blueprint)

# Authentication management
api.add_resource(AuthCredentialResource, "/auth/credential")
api.add_resource(AuthRefreshResource, "/auth/refresh")
api.add_resource(AuthCurrentResource, "/auth/current")
api.add_resource(AuthDetailsResource, "/auth/details")
api.add_resource(AuthLogoutResource, "/auth/logout")
api.add_resource(AuthTimeResource, "/auth/time")

"""
Global error handlers
"""


@blueprint.errorhandler(500)
def internal_server_error(error):
    """
    Return internal server errors with JSON
    """
    response = {
        "status": 500,
        "error": "Internal Server Error",
        "message": str(error),
        "traceback": traceback.format_exc()
    }
    return jsonify(response), 500


@blueprint.errorhandler(Exception)
def handle_exception(e):
    """
    Return internal server errors with JSON
    """
    if isinstance(e, HTTPException):
        return jsonify(error=str(e), status_code=e.code), e.code

    # JWT errors management :: BEGIN
    # Token expired
    if isinstance(e, ExpiredSignatureError):
        custom_response = {"success": False,
                           "errors": [{"ref": "jwt", "key": "jwt_token_expired", "message": str(e)}]}
        return jsonify(**custom_response), 401
    # Unable to decode JWT token
    if isinstance(e, DecodeError):
        custom_response = {"success": False,
                           "errors": [{"ref": "jwt", "key": "unable_to_decode_jwt_token", "message": str(e)}]}
        return jsonify(**custom_response), 401
    # Without Bearer token
    if isinstance(e, NoAuthorizationError):
        custom_response = {"success": False,
                           "errors": [{"ref": "jwt", "key": "jwt_token_not_present", "message": str(e)}]}
        return jsonify(**custom_response), 401
    # JWT errors management :: END

    response = {
        "status": 500,
        "error": "Internal Server Error",
        "message": str(e),
        "traceback": traceback.format_exc()
    }
    return jsonify(response), 500
