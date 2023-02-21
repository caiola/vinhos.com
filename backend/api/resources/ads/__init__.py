"""Ads Restful resources"""
from flask import Blueprint
from flask_restful import Api, Resource, marshal_with

from .resources import AdResource, AdsResource

blueprint = Blueprint("ads", __name__)
api = Api(blueprint)

api.add_resource(AdsResource, "/ads/")
api.add_resource(AdResource, "/ads/<uuid:pk>")
