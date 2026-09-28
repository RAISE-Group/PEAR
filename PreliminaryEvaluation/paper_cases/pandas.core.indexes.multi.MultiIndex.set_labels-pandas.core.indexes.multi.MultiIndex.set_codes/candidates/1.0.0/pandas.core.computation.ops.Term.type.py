@property
def type(self):
    try:
        return self._value.values.dtype
    except AttributeError:
        try:
            return self._value.dtype
        except AttributeError:
            return type(self._value)