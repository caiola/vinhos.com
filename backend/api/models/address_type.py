"""
Define the Address Type model
"""
from enum import Enum


class AddressType(Enum):
    ACCOUNT = "account"
    STORE = "store"
    USER = "user"
    # The address type "custom" can be used as billing address
    CUSTOM = "custom"
