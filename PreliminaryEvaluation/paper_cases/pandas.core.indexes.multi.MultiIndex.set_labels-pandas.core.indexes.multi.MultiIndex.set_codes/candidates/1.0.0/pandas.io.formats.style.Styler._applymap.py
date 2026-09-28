def _applymap(self, func, subset=None, **kwargs):
    func = partial(func, **kwargs)
    if subset is None:
        subset = pd.IndexSlice[:]
    subset = _non_reducing_slice(subset)
    result = self.data.loc[subset].applymap(func)
    self._update_ctx(result)
    return self