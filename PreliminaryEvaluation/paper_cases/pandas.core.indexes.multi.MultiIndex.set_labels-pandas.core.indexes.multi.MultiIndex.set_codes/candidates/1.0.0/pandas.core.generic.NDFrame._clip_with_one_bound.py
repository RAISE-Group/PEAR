def _clip_with_one_bound(self, threshold, method, axis, inplace):
    if axis is not None:
        axis = self._get_axis_number(axis)
    if is_scalar(threshold) and is_number(threshold):
        if method.__name__ == 'le':
            return self._clip_with_scalar(None, threshold, inplace=inplace)
        return self._clip_with_scalar(threshold, None, inplace=inplace)
    subset = method(threshold, axis=axis) | isna(self)
    if not isinstance(threshold, ABCSeries) and is_list_like(threshold):
        if isinstance(self, ABCSeries):
            threshold = self._constructor(threshold, index=self.index)
        else:
            threshold = _align_method_FRAME(self, threshold, axis)
    return self.where(subset, threshold, axis=axis, inplace=inplace)