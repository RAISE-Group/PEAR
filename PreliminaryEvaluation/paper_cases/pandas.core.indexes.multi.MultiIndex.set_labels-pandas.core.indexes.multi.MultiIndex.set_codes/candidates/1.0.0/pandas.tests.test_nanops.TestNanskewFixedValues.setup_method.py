def setup_method(self, method):
    self.samples = np.sin(np.linspace(0, 1, 200))
    self.actual_skew = -0.1875895205961754