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
