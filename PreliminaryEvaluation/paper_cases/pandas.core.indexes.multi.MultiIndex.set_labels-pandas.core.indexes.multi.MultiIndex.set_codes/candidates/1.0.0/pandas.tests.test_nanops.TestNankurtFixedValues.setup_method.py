def setup_method(self, method):
    self.samples = np.sin(np.linspace(0, 1, 200))
    self.actual_kurt = -1.2058303433799713