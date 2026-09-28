def take_nd(self, indexer, axis, new_mgr_locs=None, fill_tuple=None):
    """
        Take values according to indexer and return them as a block.bb

        """
    values = self.values
    if fill_tuple is None:
        fill_value = self.fill_value
        allow_fill = False
    else:
        fill_value = fill_tuple[0]
        allow_fill = True
    new_values = algos.take_nd(values, indexer, axis=axis, allow_fill=allow_fill, fill_value=fill_value)
    assert not (axis == 0 and new_mgr_locs is None)
    if new_mgr_locs is None:
        new_mgr_locs = self.mgr_locs
    if not is_dtype_equal(new_values.dtype, self.dtype):
        return self.make_block(new_values, new_mgr_locs)
    else:
        return self.make_block_same_class(new_values, new_mgr_locs)