def test_unsupported(self, fp):
    df = pd.DataFrame({'a': pd.period_range('2013', freq='M', periods=3)})
    self.check_error_on_write(df, fp, ValueError)
    df = pd.DataFrame({'a': ['a', 1, 2.0]})
    self.check_error_on_write(df, fp, ValueError)