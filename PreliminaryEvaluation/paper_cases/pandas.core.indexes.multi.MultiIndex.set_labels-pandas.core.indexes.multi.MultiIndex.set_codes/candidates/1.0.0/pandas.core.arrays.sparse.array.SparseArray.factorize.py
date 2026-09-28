def factorize(self, na_sentinel=-1):
    codes, uniques = algos.factorize(np.asarray(self), na_sentinel=na_sentinel)
    uniques = SparseArray(uniques, dtype=self.dtype)
    return (codes, uniques)