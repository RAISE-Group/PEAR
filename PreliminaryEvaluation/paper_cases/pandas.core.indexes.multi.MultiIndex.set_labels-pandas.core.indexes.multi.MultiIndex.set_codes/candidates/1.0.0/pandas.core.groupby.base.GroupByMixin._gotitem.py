def _gotitem(self, key, ndim, subset=None):
    """
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : 1,2
            requested ndim of result
        subset : object, default None
            subset to act on
        """
    if subset is None:
        subset = self.obj
    kwargs = {attr: getattr(self, attr) for attr in self._attributes}
    try:
        groupby = self._groupby[key]
    except IndexError:
        groupby = self._groupby
    self = type(self)(subset, groupby=groupby, parent=self, **kwargs)
    self._reset_cache()
    if subset.ndim == 2:
        if is_scalar(key) and key in subset or is_list_like(key):
            self._selection = key
    return self