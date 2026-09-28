def fillna(self, value, **kwargs):
    if is_integer(value):
        raise TypeError('Passing integers to fillna for timedelta64[ns] dtype is no longer supported.  To obtain the old behavior, pass `pd.Timedelta(seconds=n)` instead.')
    return super().fillna(value, **kwargs)