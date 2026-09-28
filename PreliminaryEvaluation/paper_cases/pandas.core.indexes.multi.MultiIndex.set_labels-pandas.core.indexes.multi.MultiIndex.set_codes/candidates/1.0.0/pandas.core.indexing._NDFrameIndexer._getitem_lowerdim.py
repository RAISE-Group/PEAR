def _getitem_lowerdim(self, tup: Tuple):
    if self.axis is not None:
        axis = self.obj._get_axis_number(self.axis)
        return self._getitem_axis(tup, axis=axis)
    if self._is_nested_tuple_indexer(tup):
        return self._getitem_nested_tuple(tup)
    ax0 = self.obj._get_axis(0)
    if isinstance(ax0, ABCMultiIndex) and self.name != 'iloc':
        result = self._handle_lowerdim_multi_index_axis0(tup)
        if result is not None:
            return result
    if len(tup) > self.ndim:
        raise IndexingError('Too many indexers. handle elsewhere')
    for i, key in enumerate(tup):
        if is_label_like(key) or isinstance(key, tuple):
            section = self._getitem_axis(key, axis=i)
            if not is_list_like_indexer(section):
                return section
            elif section.ndim == self.ndim:
                new_key = tup[:i] + (_NS,) + tup[i + 1:]
            else:
                new_key = tup[:i] + tup[i + 1:]
                if isinstance(section, ABCDataFrame) and i > 0 and (len(new_key) == 2):
                    a, b = new_key
                    new_key = (b, a)
                if len(new_key) == 1:
                    new_key = new_key[0]
            if com.is_null_slice(new_key):
                return section
            return getattr(section, self.name)[new_key]
    raise IndexingError('not applicable')