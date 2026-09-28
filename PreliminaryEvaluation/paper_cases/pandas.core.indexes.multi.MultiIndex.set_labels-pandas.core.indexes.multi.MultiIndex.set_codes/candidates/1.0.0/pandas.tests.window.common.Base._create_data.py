def _create_data(self):
    arr = randn(N)
    arr[self._nan_locs] = np.NaN
    self.arr = arr
    self.rng = bdate_range(datetime(2009, 1, 1), periods=N)
    self.series = Series(arr.copy(), index=self.rng)
    self.frame = DataFrame(randn(N, K), index=self.rng, columns=np.arange(K))