"""
Define the Verification Type model
"""
from enum import Enum


class VerificationType(Enum):
    USER = "user"
    EMAIL = "email"
    OTP = "otp"
