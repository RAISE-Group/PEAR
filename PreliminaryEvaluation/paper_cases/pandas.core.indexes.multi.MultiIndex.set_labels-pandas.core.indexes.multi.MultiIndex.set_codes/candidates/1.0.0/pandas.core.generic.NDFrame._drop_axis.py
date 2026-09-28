def _drop_axis(self: FrameOrSeries, labels, axis, level=None, errors: str='raise') -> FrameOrSeries:
    """
        Drop labels from specified axis. Used in the ``drop`` method
        internally.

        Parameters
        ----------
        labels : single label or list-like
        axis : int or axis name
        level : int or level name, default None
            For MultiIndex
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and existing labels are dropped.

        """
    axis = self._get_axis_number(axis)
    axis_name = self._get_axis_name(axis)
    axis = self._get_axis(axis)
    if axis.is_unique:
        if level is not None:
            if not isinstance(axis, MultiIndex):
                raise AssertionError('axis must be a MultiIndex')
            new_axis = axis.drop(labels, level=level, errors=errors)
        else:
            new_axis = axis.drop(labels, errors=errors)
        result = self.reindex(**{axis_name: new_axis})
    else:
        labels = ensure_object(com.index_labels_to_array(labels))
        if level is not None:
            if not isinstance(axis, MultiIndex):
                raise AssertionError('axis must be a MultiIndex')
            indexer = ~axis.get_level_values(level).isin(labels)
            if errors == 'raise' and indexer.all():
                raise KeyError(f'{labels} not found in axis')
        else:
            indexer = ~axis.isin(labels)
            labels_missing = (axis.get_indexer_for(labels) == -1).any()
            if errors == 'raise' and labels_missing:
                raise KeyError(f'{labels} not found in axis')
        slicer = [slice(None)] * self.ndim
        slicer[self._get_axis_number(axis_name)] = indexer
        result = self.loc[tuple(slicer)]
    return result