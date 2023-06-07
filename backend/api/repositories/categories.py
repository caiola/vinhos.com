""" Defines the categories repository """
from flask import current_app

from api.models.wine_category import WineCategory


def list(category=None):
    """Lists categories"""
    params = {}

    if category is not None:
        params["main_category_id"] = category

    current_app.logger.debug({"ENDPOINT-CALL": "categories.list().params", "params:": params, "category": category})

    return WineCategory.query.filter_by(**params).order_by(WineCategory.id.asc())
