def test_write_column_multiindex(self, engine):
    mi_columns = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])
    df = pd.DataFrame(np.random.randn(4, 3), columns=mi_columns)
    self.check_error_on_write(df, engine, ValueError)