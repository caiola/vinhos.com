"""Account Restful resources"""

from flask_restful import Resource


class AccountResource(Resource):
    """Account management: User Registration (new account, user and store)"""

    def post(self):
        """User Registration (new account, user and store)"""

        return {"company_name": "abc"}, 200
