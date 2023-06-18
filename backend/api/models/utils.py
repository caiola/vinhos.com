from typing import Any


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
    if bool(key) is False or bool(message) is False or type(errors) != list or type(key) != str:
        return
    errors += [{"ref": key, "message": message}]
