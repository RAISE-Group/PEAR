def _codes_to_ints(self, codes):
    """
        Transform combination(s) of uint64 in one Python integer (each), in a
        strictly monotonic way (i.e. respecting the lexicographic order of
        integer combinations): see BaseMultiIndexCodesEngine documentation.

        Parameters
        ----------
        codes : 1- or 2-dimensional array of dtype uint64
            Combinations of integers (one per row)

        Returns
        -------
        int, or 1-dimensional array of dtype object
            Integer(s) representing one combination (each).
        """
    codes = codes.astype('object') << self.offsets
    if codes.ndim == 1:
        return np.bitwise_or.reduce(codes)
    return np.bitwise_or.reduce(codes, axis=1)