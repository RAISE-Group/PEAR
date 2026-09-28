def __getitem__(self, item):
    if pd.api.types.is_scalar(item):
        return self._data.to_pandas()[item]
    else:
        vals = self._data.to_pandas()[item]
        return type(self).from_scalars(vals)