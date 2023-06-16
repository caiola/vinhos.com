from typing import Any


def get_value(data, key, default=None) -> Any:
    """Get value"""
    if data is None:
        return default
    try:
        return data[key]
    except AttributeError:
        return default
    except KeyError:
        return default
    except TypeError:
        return default


def add_error(errors, key, message) -> Any:
    errors += [
        {"ref": key, "message": message}
    ]
