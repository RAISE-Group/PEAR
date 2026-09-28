def _add_nat(self):
    """
        Add pd.NaT to self
        """
    if is_period_dtype(self):
        raise TypeError(f'Cannot add {type(self).__name__} and {type(NaT).__name__}')
    result = np.zeros(self.shape, dtype=np.int64)
    result.fill(iNaT)
    return type(self)(result, dtype=self.dtype, freq=None)