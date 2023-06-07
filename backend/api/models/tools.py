class utils:
    def v(data, key):
        """Get value"""
        try:
            if data is None:
                return None
            return data[key]
        except KeyError:
            return None
        except Exception:
            return None
