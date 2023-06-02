"""Categories Restful resources"""

from flask import url_for, current_app, request
from flask_jwt_extended import jwt_required
from flask_restful import marshal_with, reqparse

from api.repositories import categories
from api.resources.base_resource import BaseResource
from api.resources.categories.serializers import ListSerializer

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


class CategoriesResource(BaseResource):
    """Categories list"""

    @jwt_required()
    @marshal_with(ListSerializer)
    def get(self, category=None):
        """Get all categories by category if defined"""
        args = list_resource_parser.parse_args()
        pagination = categories.list(category=category).paginate(page=args["page"], per_page=args["size"])

        return {
            "cid": self.get_correlation_id(request.headers, args),
            "total": pagination.total,
            "previous": url_for(
                "categories.categoriesresource", page=args["page"] - 1, size=args["size"], category=category
            )
            if pagination.has_prev
            else None,
            "next": url_for("categories.categoriesresource", page=args["page"] + 1, size=args["size"], category=category)
            if pagination.has_next
            else None,
            "results": pagination.items,
        }
