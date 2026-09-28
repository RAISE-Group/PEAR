def setup_method(self, method):
    self.series = Series(np.arange(10))
    self.frame = DataFrame({'A': [1] * 20 + [2] * 12 + [3] * 8, 'B': np.arange(40)})