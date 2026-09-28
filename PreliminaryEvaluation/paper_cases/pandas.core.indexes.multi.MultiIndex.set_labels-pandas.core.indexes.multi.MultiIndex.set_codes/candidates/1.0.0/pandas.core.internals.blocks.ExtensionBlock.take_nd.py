def take_nd(self, indexer, axis=0, new_mgr_locs=None, fill_tuple=None):
    """
        Take values according to indexer and return them as a block.
        """
    if fill_tuple is None:
        fill_value = None
    else:
        fill_value = fill_tuple[0]
    new_values = self.values.take(indexer, fill_value=fill_value, allow_fill=True)
    assert not (self.ndim == 1 and new_mgr_locs is None)
    if new_mgr_locs is None:
        new_mgr_locs = self.mgr_locs
    return self.make_block_same_class(new_values, new_mgr_locs)