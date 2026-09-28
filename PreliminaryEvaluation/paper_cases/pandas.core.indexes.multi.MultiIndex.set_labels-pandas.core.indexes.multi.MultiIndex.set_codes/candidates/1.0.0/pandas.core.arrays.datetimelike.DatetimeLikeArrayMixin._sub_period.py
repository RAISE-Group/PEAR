def _sub_period(self, other):
    raise TypeError(f'cannot subtract Period from a {type(self).__name__}')