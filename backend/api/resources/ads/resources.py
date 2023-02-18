"""Ads Restful resources"""
from flask import url_for
from flask_restful import Api, Resource, marshal_with, reqparse

from api.repositories import ads

from .serializers import AdSerializer, ListSerializer

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
