def setup_method(self, method):
    self.variance = variance = 3.0
    self.samples = self.prng.normal(scale=variance ** 0.5, size=100000)