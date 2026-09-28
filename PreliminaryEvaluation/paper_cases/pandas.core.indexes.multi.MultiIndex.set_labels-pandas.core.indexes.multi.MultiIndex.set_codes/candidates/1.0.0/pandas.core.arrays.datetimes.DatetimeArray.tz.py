@tz.setter
def tz(self, value):
    raise AttributeError('Cannot directly set timezone. Use tz_localize() or tz_convert() as appropriate')