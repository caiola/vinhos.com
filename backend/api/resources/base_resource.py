"""Base resource with extended properties to parse payload"""

from flask_restful import Resource
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import HTTPException


class BaseResource(Resource):
    """Base resource"""

    def v(self, data, key):
        """Get value"""
        try:
            return data[key]
        except KeyError:
            return None

    def a(self, data, key):
        """Get attribute"""
        return getattr(data, key, None)

    def execute_parse_args(self, resource_parser):
        """Parse args from the payload"""
        errors = None
        try:
            resource_parser.parse_args(req=None, strict=True, http_error_code=400)
        except HTTPException or BadRequest as e:
            # If flask_restful.abort is modified to include 'data' attribute with errors
            try:
                errors = e.data
            except AttributeError as e2:
                errors = {"message": {"payload": "Invalid payload"}}
        except Exception as e:
            errors = {"message": {"unknown": "unknown: " + str(e)}}

        return errors
