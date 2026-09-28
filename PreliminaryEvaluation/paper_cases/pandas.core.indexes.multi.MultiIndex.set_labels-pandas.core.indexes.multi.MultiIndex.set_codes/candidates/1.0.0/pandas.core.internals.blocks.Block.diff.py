def diff(self, n: int, axis: int=1) -> List['Block']:
    """ return block for the diff of the values """
    new_values = algos.diff(self.values, n, axis=axis, stacklevel=7)
    new_values = _block_shape(new_values, ndim=self.ndim)
    return [self.make_block(values=new_values)]