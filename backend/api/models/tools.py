from typing import Any

from flask import current_app


class utils:
    def get_value(self, data, key, default=None) -> Any:
        """Get value"""
        if data is None:
            return default
        try:
            return data[key]
        except KeyError:
            return default
        except TypeError:
            current_app.logger.debug({
                "FUNCTION-CALL": "utils.get_value()",
                "data": data,
                "key": key,
                "default": default
            })
            return data.get(key)

    def error(self, key, message) -> Any:
        return {"ref": key, "message": message}

    def add_error(self, errors, key, message) -> Any:
        errors += [
            utils().error(key, message)
        ]
