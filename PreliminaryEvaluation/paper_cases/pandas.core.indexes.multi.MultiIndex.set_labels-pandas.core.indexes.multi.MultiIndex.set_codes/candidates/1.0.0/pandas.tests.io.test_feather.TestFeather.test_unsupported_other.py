def test_unsupported_other(self):
    df = pd.DataFrame({'a': pd.period_range('2013', freq='M', periods=3)})
    self.check_error_on_write(df, Exception)