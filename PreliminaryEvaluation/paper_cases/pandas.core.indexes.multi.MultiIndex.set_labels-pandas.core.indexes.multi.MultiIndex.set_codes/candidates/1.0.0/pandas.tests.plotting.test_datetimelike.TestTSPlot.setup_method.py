def setup_method(self, method):
    TestPlotBase.setup_method(self, method)
    self.freq = ['S', 'T', 'H', 'D', 'W', 'M', 'Q', 'A']
    idx = [period_range('12/31/1999', freq=x, periods=100) for x in self.freq]
    self.period_ser = [Series(np.random.randn(len(x)), x) for x in idx]
    self.period_df = [DataFrame(np.random.randn(len(x), 3), index=x, columns=['A', 'B', 'C']) for x in idx]
    freq = ['S', 'T', 'H', 'D', 'W', 'M', 'Q-DEC', 'A', '1B30Min']
    idx = [date_range('12/31/1999', freq=x, periods=100) for x in freq]
    self.datetime_ser = [Series(np.random.randn(len(x)), x) for x in idx]
    self.datetime_df = [DataFrame(np.random.randn(len(x), 3), index=x, columns=['A', 'B', 'C']) for x in idx]