"""Restful resources"""
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from flask_jwt_extended.exceptions import NoAuthorizationError
from .resources import RegionsResource
from jwt.exceptions import ExpiredSignatureError, DecodeError
from werkzeug.exceptions import UnsupportedMediaType

blueprint = Blueprint("regions", __name__)
api = Api(blueprint)

# Regions management
api.add_resource(RegionsResource, "/regions")

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
    if isinstance(e, UnsupportedMediaType):
        custom_response = {"success": False,
                           "errors": [{"ref": "payload", "key": "invalid_json", "message": str(e)}]}
        return jsonify(**custom_response), 400

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
