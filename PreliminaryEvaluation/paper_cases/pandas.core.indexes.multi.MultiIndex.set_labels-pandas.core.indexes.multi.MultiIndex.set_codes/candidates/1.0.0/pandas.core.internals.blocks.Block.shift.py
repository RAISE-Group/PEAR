def shift(self, periods, axis=0, fill_value=None):
    """ shift the block by periods, possibly upcast """
    new_values, fill_value = maybe_upcast(self.values, fill_value)
    f_ordered = new_values.flags.f_contiguous
    if f_ordered:
        new_values = new_values.T
        axis = new_values.ndim - axis - 1
    if np.prod(new_values.shape):
        new_values = np.roll(new_values, ensure_platform_int(periods), axis=axis)
    axis_indexer = [slice(None)] * self.ndim
    if periods > 0:
        axis_indexer[axis] = slice(None, periods)
    else:
        axis_indexer[axis] = slice(periods, None)
    new_values[tuple(axis_indexer)] = fill_value
    if f_ordered:
        new_values = new_values.T
    return [self.make_block(new_values)]