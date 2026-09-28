def setup_method(self, method):
    self.df = DataFrame({'A': [1, 2, 3]})
    self.expected1 = self.df[self.df.A > 0]
    self.expected2 = self.df.A + 1