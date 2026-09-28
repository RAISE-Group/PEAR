def _ixs(self, i: int, axis: int=0):
    """
        Parameters
        ----------
        i : int
        axis : int

        Notes
        -----
        If slice passed, the resulting data will be a view.
        """
    if axis == 0:
        new_values = self._data.fast_xs(i)
        copy = isinstance(new_values, np.ndarray) and new_values.base is None
        result = self._constructor_sliced(new_values, index=self.columns, name=self.index[i], dtype=new_values.dtype)
        result._set_is_copy(self, copy=copy)
        return result
    else:
        label = self.columns[i]
        values = self._data.iget(i)
        if len(self.index) and (not len(values)):
            values = np.array([np.nan] * len(self.index), dtype=object)
        result = self._box_col_values(values, label)
        result._set_as_cached(label, self)
        return result