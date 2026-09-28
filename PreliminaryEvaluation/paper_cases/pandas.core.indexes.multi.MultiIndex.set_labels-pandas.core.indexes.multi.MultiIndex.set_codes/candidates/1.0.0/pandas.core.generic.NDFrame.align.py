@Appender(_shared_docs['align'] % _shared_doc_kwargs)
def align(self, other, join='outer', axis=None, level=None, copy=True, fill_value=None, method=None, limit=None, fill_axis=0, broadcast_axis=None):
    method = missing.clean_fill_method(method)
    if broadcast_axis == 1 and self.ndim != other.ndim:
        if isinstance(self, ABCSeries):
            cons = self._constructor_expanddim
            df = cons({c: self for c in other.columns}, **other._construct_axes_dict())
            return df._align_frame(other, join=join, axis=axis, level=level, copy=copy, fill_value=fill_value, method=method, limit=limit, fill_axis=fill_axis)
        elif isinstance(other, ABCSeries):
            cons = other._constructor_expanddim
            df = cons({c: other for c in self.columns}, **self._construct_axes_dict())
            return self._align_frame(df, join=join, axis=axis, level=level, copy=copy, fill_value=fill_value, method=method, limit=limit, fill_axis=fill_axis)
    if axis is not None:
        axis = self._get_axis_number(axis)
    if isinstance(other, ABCDataFrame):
        return self._align_frame(other, join=join, axis=axis, level=level, copy=copy, fill_value=fill_value, method=method, limit=limit, fill_axis=fill_axis)
    elif isinstance(other, ABCSeries):
        return self._align_series(other, join=join, axis=axis, level=level, copy=copy, fill_value=fill_value, method=method, limit=limit, fill_axis=fill_axis)
    else:
        raise TypeError(f'unsupported type: {type(other)}')