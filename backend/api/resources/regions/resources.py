"""Regions Restful resources"""

from api.repositories import regions
from api.resources.base_resource import BaseResource


class RegionsResource(BaseResource):
    """Regions management"""

    def get(self):
        """Regions"""

        # if request.is_json:
        #     data = request.get_json()
        # else:
        #     data = None
        #
        # result = accounts.registration(data)
        #
        # # Do not send password_hash
        # try:
        #     result.pop("password_hash", None)
        # except Exception as e:
        #     pass

        result = regions.all()

        return result, 201
