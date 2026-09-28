@classmethod
def _from_name(cls, *args):
    return cls(**cls._parse_suffix(*args))