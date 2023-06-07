"""Base resource with extended properties to parse payload"""
import uuid

from flask_restful import Resource
from werkzeug.exceptions import BadRequest, HTTPException


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

    def get_correlation_id(self, headers, args):
        if headers is None:
            return False

        # This dependends on the hosting platform e.g. AWS, GCP, Azure have different header for the correlation id
        correlation_id = headers.get('X-Correlation-ID')

        if correlation_id is None:
            correlation_id = uuid.uuid4()

        return correlation_id
