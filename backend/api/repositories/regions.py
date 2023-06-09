""" Defines the regions repository """
from flask import current_app

from api.models.wine_region import WineRegion


def list(country=None):
    """Lists regions"""
    params = {}

    # If not defined assume "pt" country
    if country is None:
        params["country"] = "pt"
    else:
        # Get the first two chars from string
        params["country"] = str(country)[:2]

    current_app.logger.debug(
        {
            "ENDPOINT-CALL": "regions.list().params",
            "params:": params,
            "country": country,
        }
    )

    return WineRegion.query.filter_by(**params).order_by(WineRegion.id.asc())
