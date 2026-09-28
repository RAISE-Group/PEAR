def _setitem_with_indexer_missing(self, indexer, value):
    """
        Insert new row(s) or column(s) into the Series or DataFrame.
        """
    from pandas import Series
    if self.ndim == 1:
        index = self.obj.index
        new_index = index.insert(len(index), indexer)
        if index.is_unique:
            new_indexer = index.get_indexer([new_index[-1]])
            if (new_indexer != -1).any():
                return self._setitem_with_indexer(new_indexer, value)
        new_values = Series([value])._values
        if len(self.obj._values):
            new_values = concat_compat([self.obj._values, new_values])
        self.obj._data = self.obj._constructor(new_values, index=new_index, name=self.obj.name)._data
        self.obj._maybe_update_cacher(clear=True)
        return self.obj
    elif self.ndim == 2:
        if not len(self.obj.columns):
            raise ValueError('cannot set a frame with no defined columns')
        if isinstance(value, ABCSeries):
            value = value.reindex(index=self.obj.columns, copy=True)
            value.name = indexer
        else:
            if is_list_like_indexer(value):
                if len(value) != len(self.obj.columns):
                    raise ValueError('cannot set a row with mismatched columns')
            value = Series(value, index=self.obj.columns, name=indexer)
        self.obj._data = self.obj.append(value)._data
        self.obj._maybe_update_cacher(clear=True)
        return self.obj