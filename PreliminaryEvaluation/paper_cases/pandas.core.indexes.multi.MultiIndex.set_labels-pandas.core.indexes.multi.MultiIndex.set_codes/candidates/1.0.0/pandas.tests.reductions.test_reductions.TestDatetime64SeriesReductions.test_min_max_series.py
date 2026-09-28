def test_min_max_series(self):
    rng = pd.date_range('1/1/2000', periods=10, freq='4h')
    lvls = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    df = DataFrame({'TS': rng, 'V': np.random.randn(len(rng)), 'L': lvls})
    result = df.TS.max()
    exp = pd.Timestamp(df.TS.iat[-1])
    assert isinstance(result, pd.Timestamp)
    assert result == exp
    result = df.TS.min()
    exp = pd.Timestamp(df.TS.iat[0])
    assert isinstance(result, pd.Timestamp)
    assert result == exp