def test_df_use_case(self):
    df = DataFrame({'a': np.random.randn(10), 'b': np.random.randn(10)})
    df.eval('e = arctan2(sin(a), b)', engine=self.engine, parser=self.parser, inplace=True)
    got = df.e
    expect = np.arctan2(np.sin(df.a), df.b)
    tm.assert_series_equal(got, expect, check_names=False)