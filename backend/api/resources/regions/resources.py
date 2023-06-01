"""Regions Restful resources"""

from flask import url_for, json
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
    default=10,
    help="Number of records per page",
    required=False,
    location="args",
)


class RegionsResource(BaseResource):
    """Regions management"""

    @jwt_required()
    @marshal_with(ListSerializer)
    def get(self):
        # """Get all regions"""
        args = list_resource_parser.parse_args()
        pagination = regions.list().paginate(page=args["page"], per_page=args["size"])

        return {
            "total": pagination.total,
            "previous": url_for(
                "regions.regionsresource", page=args["page"] - 1, size=args["size"]
            )
            if pagination.has_prev
            else None,
            "next": url_for("regions.regionsresource", page=args["page"] + 1, size=args["size"])
            if pagination.has_next
            else None,
            "results": pagination.items,
        }


#
class RegionsByCountryResource(BaseResource):
    """Get regions by country"""

    def get(self, country):
        """Get all regions by country"""

        # result = list(regions.get_by_country(country=country))

        # return result, 200

        args = list_resource_parser.parse_args()
        pagination = regions.list().paginate(page=args["page"], per_page=args["size"])

        return json.dumps(list(pagination.items))
        # return {
        #     "total": pagination.total,
        #     "previous": url_for(
        #         "regions.regionsresource", page=args["page"] - 1, size=args["size"]
        #     )
        #     if pagination.has_prev
        #     else None,
        #     "next": url_for("regions.regionsresource", page=args["page"] + 1, size=args["size"])
        #     if pagination.has_next
        #     else None,
        #     "results": pagination.items,
        # }
