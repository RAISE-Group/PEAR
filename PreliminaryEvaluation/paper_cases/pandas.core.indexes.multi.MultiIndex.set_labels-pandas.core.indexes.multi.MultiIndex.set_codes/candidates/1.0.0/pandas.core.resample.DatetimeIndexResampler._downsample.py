def _downsample(self, how, **kwargs):
    """
        Downsample the cython defined function.

        Parameters
        ----------
        how : string / cython mapped function
        **kwargs : kw args passed to how function
        """
    self._set_binner()
    how = self._get_cython_func(how) or how
    ax = self.ax
    obj = self._selected_obj
    if not len(ax):
        obj = obj.copy()
        obj.index._set_freq(self.freq)
        return obj
    if ax.freq is not None or ax.inferred_freq is not None:
        if len(self.grouper.binlabels) > len(ax) and how is None:
            return self.asfreq()
    result = obj.groupby(self.grouper, axis=self.axis).aggregate(how, **kwargs)
    result = self._apply_loffset(result)
    return self._wrap_result(result)