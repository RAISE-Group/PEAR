def concat_same_type(self, to_concat, placement=None):
    """
        Always concatenate disregarding self.ndim as the values are
        always 1D in this custom Block
        """
    values = np.concatenate([blk.values for blk in to_concat])
    return self.make_block_same_class(values, placement=placement or slice(0, len(values), 1))