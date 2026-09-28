def __eq__(self, other):
    if is_list_like(other):
        if len(self) != len(other):
            raise ValueError('Lengths must match to compare')
        other = array(other)
    elif not isinstance(other, Interval):
        return np.zeros(len(self), dtype=bool)
    if isinstance(other, Interval):
        other_dtype = 'interval'
    elif not is_categorical_dtype(other):
        other_dtype = other.dtype
    else:
        other_dtype = other.categories.dtype
        if is_interval_dtype(other_dtype):
            if self.closed != other.categories.closed:
                return np.zeros(len(self), dtype=bool)
            other = other.categories.take(other.codes)
    if is_interval_dtype(other_dtype):
        if self.closed != other.closed:
            return np.zeros(len(self), dtype=bool)
        return (self.left == other.left) & (self.right == other.right)
    if not is_object_dtype(other_dtype):
        return np.zeros(len(self), dtype=bool)
    result = np.zeros(len(self), dtype=bool)
    for i, obj in enumerate(other):
        if isinstance(obj, Interval) and self.closed == obj.closed and (self.left[i] == obj.left) and (self.right[i] == obj.right):
            result[i] = True
    return result