def test_columns_dtypes_invalid(self, engine):
    df = pd.DataFrame({'string': list('abc'), 'int': list(range(1, 4))})
    df.columns = [0, 1]
    self.check_error_on_write(df, engine, ValueError)
    df.columns = [b'foo', b'bar']
    self.check_error_on_write(df, engine, ValueError)
    df.columns = [datetime.datetime(2011, 1, 1, 0, 0), datetime.datetime(2011, 1, 1, 1, 1)]
    self.check_error_on_write(df, engine, ValueError)