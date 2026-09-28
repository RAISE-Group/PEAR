def isna(self):
    nas = pd.isna(self._data.to_pandas())
    return type(self).from_scalars(nas)