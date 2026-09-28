def _sub_datetimelike_scalar(self, other):
    assert other is not NaT
    raise TypeError(f'cannot subtract a datelike from a {type(self).__name__}')