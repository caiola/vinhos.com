from typing import Any

from api import db


def get_value(data: Any, key: str, default=None) -> Any:
    """Get value"""
    if data is None:
        return default
    try:
        return data[key]
    except TypeError:
        return getattr(data, key, default)
    except KeyError:
        return default


def add_error(errors: list, key: str, message: str):
    if (
            bool(key) is False
            or bool(message) is False
            or type(errors) != list
            or type(key) != str
    ):
        return
    errors.append({"ref": key, "message": message})


def lowercase_enum(enum_class):
    return db.Enum(*(item.value.lower() for item in enum_class), name="lowercase_enum")
