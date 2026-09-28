def test_std_var_pass_ddof(self):
    index = MultiIndex.from_arrays([np.arange(5).repeat(10), np.tile(np.arange(10), 5)])
    df = DataFrame(np.random.randn(len(index), 5), index=index)
    for meth in ['var', 'std']:
        ddof = 4
        alt = lambda x: getattr(x, meth)(ddof=ddof)
        result = getattr(df[0], meth)(level=0, ddof=ddof)
        expected = df[0].groupby(level=0).agg(alt)
        tm.assert_series_equal(result, expected)
        result = getattr(df, meth)(level=0, ddof=ddof)
        expected = df.groupby(level=0).agg(alt)
        tm.assert_frame_equal(result, expected)