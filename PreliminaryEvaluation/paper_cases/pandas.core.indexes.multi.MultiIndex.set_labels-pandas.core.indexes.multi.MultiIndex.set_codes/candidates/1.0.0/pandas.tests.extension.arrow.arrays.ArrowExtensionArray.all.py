def all(self, axis=0, out=None):
    return self._data.to_pandas().all()