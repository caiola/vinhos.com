""" Defines the Account repository """

from api.models import Account


def get_by(pk: int = None, name: str = None) -> Account:
    """Query a account by uuid or id"""

    params = {}
    if (not pk and not name) or (pk and name):
        raise ValueError("Provide pk or name")

    if name:
        params["name"] = str(name)

    if pk:
        params["pk"] = pk

    return Account.query.filter_by(**params).one()


def update(account: Account, **kwargs) -> Account:
    """Update account"""
    account.update(kwargs)
    return account.save()


def create(account_name: str, company_name: str) -> Account:
    """Create a new account"""
    account = Account(account_name=account_name, company_name=company_name)

    return account.save()

# import os
#
# from flask import Flask
# from flask_jwt_extended import JWTManager, create_access_token
#
# from api.models import Ad, User, Account
#
# app = Flask(__name__)
# app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  # Set your own secret key
# jwt = JWTManager(app)


# @app.route("/login", methods=["POST"])
# def login(username: str, password: str):
#     # Assuming you have validated the user"s credentials and retrieved the user object
#     # user = get_user()  # Replace this with your own logic
#
#     # Generate the access token
#     # access_token = create_access_token(identity=user.id)
#     access_token = create_access_token(identity=123)
#
#     # Return the access token as a response
#     return {"access_token": access_token}, 200
