@Appender(Index.insert.__doc__)
def insert(self, loc, item):
    if is_scalar(item) and isna(item):
        item = self._na_value
    return super().insert(loc, item)