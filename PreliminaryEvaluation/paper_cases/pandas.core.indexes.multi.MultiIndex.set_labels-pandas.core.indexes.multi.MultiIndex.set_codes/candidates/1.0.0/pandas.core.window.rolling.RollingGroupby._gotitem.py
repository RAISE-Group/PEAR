def _gotitem(self, key, ndim, subset=None):
    if self.on is not None:
        self._groupby.obj = self._groupby.obj.set_index(self._on)
        self.on = None
    return super()._gotitem(key, ndim, subset=subset)