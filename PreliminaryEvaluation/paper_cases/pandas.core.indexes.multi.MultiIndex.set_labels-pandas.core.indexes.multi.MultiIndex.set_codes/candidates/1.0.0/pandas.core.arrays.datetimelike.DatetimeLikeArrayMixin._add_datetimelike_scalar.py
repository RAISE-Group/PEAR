def _add_datetimelike_scalar(self, other):
    raise TypeError(f'cannot add {type(self).__name__} and {type(other).__name__}')