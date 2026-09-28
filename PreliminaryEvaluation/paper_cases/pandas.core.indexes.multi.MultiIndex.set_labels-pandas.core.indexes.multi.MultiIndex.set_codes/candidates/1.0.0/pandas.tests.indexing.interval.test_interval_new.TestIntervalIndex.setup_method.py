def setup_method(self, method):
    self.s = Series(np.arange(5), IntervalIndex.from_breaks(np.arange(6)))