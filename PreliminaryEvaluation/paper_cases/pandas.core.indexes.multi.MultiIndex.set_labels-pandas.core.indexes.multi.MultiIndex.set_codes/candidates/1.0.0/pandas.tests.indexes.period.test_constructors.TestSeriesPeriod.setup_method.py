def setup_method(self, method):
    self.series = Series(period_range('2000-01-01', periods=10, freq='D'))