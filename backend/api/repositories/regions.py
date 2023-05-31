""" Defines the regions repository """

from api.models.wine_region import WineRegion


def all():
    return WineRegion.query.all()
