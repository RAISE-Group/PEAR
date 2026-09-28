@classmethod
def construct_from_string(cls, string):
    if string == cls.name:
        return cls()
    else:
        raise TypeError(f"Cannot construct a '{cls.__name__}' from '{string}'")