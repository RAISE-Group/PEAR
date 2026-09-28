def check_result_type(self, dtype, expect_dtype):
    df = DataFrame({'a': np.random.randn(10).astype(dtype)})
    assert df.a.dtype == dtype
    df.eval('b = sin(a)', engine=self.engine, parser=self.parser, inplace=True)
    got = df.b
    expect = np.sin(df.a)
    assert expect.dtype == got.dtype
    assert expect_dtype == got.dtype
    tm.assert_series_equal(got, expect, check_names=False)