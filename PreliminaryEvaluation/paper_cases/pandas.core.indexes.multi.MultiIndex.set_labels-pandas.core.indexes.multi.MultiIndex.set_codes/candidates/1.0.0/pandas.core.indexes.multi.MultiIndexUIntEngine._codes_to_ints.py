def _codes_to_ints(self, codes):
    """
        Transform combination(s) of uint64 in one uint64 (each), in a strictly
        monotonic way (i.e. respecting the lexicographic order of integer
        combinations): see BaseMultiIndexCodesEngine documentation.

        Parameters
        ----------
        codes : 1- or 2-dimensional array of dtype uint64
            Combinations of integers (one per row)

        Returns
        -------
        scalar or 1-dimensional array, of dtype uint64
            Integer(s) representing one combination (each).
        """
    codes <<= self.offsets
    if codes.ndim == 1:
        return np.bitwise_or.reduce(codes)
    return np.bitwise_or.reduce(codes, axis=1)