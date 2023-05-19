"""Ads Restful resources"""
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from .resources import AdResource, AdsResource, AccountResource, LoginResource

blueprint = Blueprint("ads", __name__)
api = Api(blueprint)

# Ad management
api.add_resource(AdsResource, "/ads/")
api.add_resource(AdResource, "/ads/<uuid:pk>")

# Account management
api.add_resource(AccountResource, "/account/")

# Login management
api.add_resource(LoginResource, "/login/")

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

    response = {
        "status": 500,
        "error": "Internal Server Error",
        "message": str(e),
        "traceback": traceback.format_exc()
    }
    return jsonify(response), 500
