def setup_method(self, method):
    self.frame = DataFrame(np.random.randn(10, 3), columns=list('abc'))