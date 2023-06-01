""" Defines the regions repository """

from flask_jwt_extended import jwt_required

from api.models.wine_region import WineRegion


# @jwt_required()
def list():
    """Lists regions"""

    return WineRegion.query.order_by(WineRegion.id.desc())


def get_all() -> WineRegion:
    params = {}

    for region in WineRegion.query.filter_by(**params).all():
        yield {"id": region.id, "name": region.name}


def get_by_country(country):
    params = {}
    if country is not None:
        params["country"] = "pt"
    if country:
        # Get the first two chars from string
        params["country"] = str(country)[:2]

    for region in WineRegion.query.filter_by(**params).all():
        yield {"id": region.id, "name": region.name}
