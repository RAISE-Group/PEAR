def _drop_labels_or_levels(self, keys, axis: int=0):
    """
        Drop labels and/or levels for the given `axis`.

        For each key in `keys`:
          - (axis=0): If key matches a column label then drop the column.
            Otherwise if key matches an index level then drop the level.
          - (axis=1): If key matches an index label then drop the row.
            Otherwise if key matches a column level then drop the level.

        Parameters
        ----------
        keys: str or list of str
            labels or levels to drop
        axis: int, default 0
            Axis that levels are associated with (0 for index, 1 for columns)

        Returns
        -------
        dropped: DataFrame

        Raises
        ------
        ValueError
            if any `keys` match neither a label nor a level
        """
    axis = self._get_axis_number(axis)
    keys = com.maybe_make_list(keys)
    invalid_keys = [k for k in keys if not self._is_label_or_level_reference(k, axis=axis)]
    if invalid_keys:
        raise ValueError(f'The following keys are not valid labels or levels for axis {axis}: {invalid_keys}')
    levels_to_drop = [k for k in keys if self._is_level_reference(k, axis=axis)]
    labels_to_drop = [k for k in keys if not self._is_level_reference(k, axis=axis)]
    dropped = self.copy()
    if axis == 0:
        if levels_to_drop:
            dropped.reset_index(levels_to_drop, drop=True, inplace=True)
        if labels_to_drop:
            dropped.drop(labels_to_drop, axis=1, inplace=True)
    else:
        if levels_to_drop:
            if isinstance(dropped.columns, MultiIndex):
                dropped.columns = dropped.columns.droplevel(levels_to_drop)
            else:
                dropped.columns = RangeIndex(dropped.columns.size)
        if labels_to_drop:
            dropped.drop(labels_to_drop, axis=0, inplace=True)
    return dropped