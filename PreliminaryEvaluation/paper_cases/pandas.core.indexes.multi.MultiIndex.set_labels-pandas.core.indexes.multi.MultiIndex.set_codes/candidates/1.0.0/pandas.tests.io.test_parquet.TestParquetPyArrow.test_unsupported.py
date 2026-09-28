def test_unsupported(self, pa):
    if LooseVersion(pyarrow.__version__) < LooseVersion('0.15.1.dev'):
        df = pd.DataFrame({'a': pd.period_range('2013', freq='M', periods=3)})
        self.check_error_on_write(df, pa, Exception)
    df = pd.DataFrame({'a': pd.timedelta_range('1 day', periods=3)})
    self.check_error_on_write(df, pa, NotImplementedError)
    df = pd.DataFrame({'a': ['a', 1, 2.0]})
    self.check_error_on_write(df, pa, Exception)