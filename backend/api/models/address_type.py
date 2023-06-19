"""
Define the Address Type model
"""
from enum import Enum


class AddressType(Enum):
    ACCOUNT = "account"
    STORE = "store"
    USER = "user"
    BILLING = "billing"
    PICKUP = "pickup"


class AddressTypeLowercase(Enum):
    def __call__(self, *args, **kwargs):
        return str(self.name).lower()
