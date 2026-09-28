def __setitem__(self, key, value):
    if pd.api.types.is_list_like(value):
        if pd.api.types.is_scalar(key):
            raise ValueError('setting an array element with a sequence.')
        value = [decimal.Decimal(v) for v in value]
    else:
        value = decimal.Decimal(value)
    self._data[key] = value