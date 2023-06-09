"""Regions Restful resources"""

from flask import current_app, request, url_for
from flask_jwt_extended import jwt_required
from flask_restful import marshal_with, reqparse

from api.repositories import regions
from api.resources.base_resource import BaseResource
from api.resources.regions.serializers import ListSerializer

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


class RegionsResource(BaseResource):
    """Regions list"""

    @jwt_required()
    @marshal_with(ListSerializer)
    def get(self, country=None):
        """Get all regions by country if defined"""
        args = list_resource_parser.parse_args()
        pagination = regions.list(country=country).paginate(
            page=args["page"], per_page=args["size"]
        )

        return {
            "cid": self.get_correlation_id(request.headers, args),
            "total": pagination.total,
            "previous": url_for(
                "regions.regionsresource",
                page=args["page"] - 1,
                size=args["size"],
                country=country,
            )
            if pagination.has_prev
            else None,
            "next": url_for(
                "regions.regionsresource",
                page=args["page"] + 1,
                size=args["size"],
                country=country,
            )
            if pagination.has_next
            else None,
            "results": pagination.items,
        }
