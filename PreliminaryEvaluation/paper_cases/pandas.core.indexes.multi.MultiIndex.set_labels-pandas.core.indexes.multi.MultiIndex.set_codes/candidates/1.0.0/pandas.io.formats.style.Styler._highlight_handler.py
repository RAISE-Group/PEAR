def _highlight_handler(self, subset=None, color='yellow', axis=None, max_=True):
    subset = _non_reducing_slice(_maybe_numeric_slice(self.data, subset))
    self.apply(self._highlight_extrema, color=color, axis=axis, subset=subset, max_=max_)
    return self