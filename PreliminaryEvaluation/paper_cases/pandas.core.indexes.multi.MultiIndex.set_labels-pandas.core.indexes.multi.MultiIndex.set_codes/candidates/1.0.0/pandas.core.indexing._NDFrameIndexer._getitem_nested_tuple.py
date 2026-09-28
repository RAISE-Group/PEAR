def _getitem_nested_tuple(self, tup: Tuple):
    if len(tup) > self.ndim:
        result = self._handle_lowerdim_multi_index_axis0(tup)
        if result is not None:
            return result
        axis = self.axis or 0
        return self._getitem_axis(tup, axis=axis)
    obj = self.obj
    axis = 0
    for i, key in enumerate(tup):
        if com.is_null_slice(key):
            axis += 1
            continue
        current_ndim = obj.ndim
        obj = getattr(obj, self.name)._getitem_axis(key, axis=axis)
        axis += 1
        if is_scalar(obj) or not hasattr(obj, 'ndim'):
            break
        if obj.ndim < current_ndim:
            axis -= 1
    return obj