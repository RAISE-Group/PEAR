def test_scalar(self):
    N = 30
    rng = date_range('1/1/1990', periods=N, freq='53s')
    ts = Series(np.arange(N), index=rng)
    ts[5:10] = np.NaN
    ts[15:20] = np.NaN
    val1 = ts.asof(ts.index[7])
    val2 = ts.asof(ts.index[19])
    assert val1 == ts[4]
    assert val2 == ts[14]
    val1 = ts.asof(str(ts.index[7]))
    assert val1 == ts[4]
    result = ts.asof(ts.index[3])
    assert result == ts[3]
    d = ts.index[0] - offsets.BDay()
    assert np.isnan(ts.asof(d))