def test_periodindex(self):
    from pandas import period_range, PeriodIndex
    N = 50
    rng = period_range('1/1/1990', periods=N, freq='H')
    ts = Series(np.random.randn(N), index=rng)
    ts[15:30] = np.nan
    dates = date_range('1/1/1990', periods=N * 3, freq='37min')
    result = ts.asof(dates)
    assert notna(result).all()
    lb = ts.index[14]
    ub = ts.index[30]
    result = ts.asof(list(dates))
    assert notna(result).all()
    lb = ts.index[14]
    ub = ts.index[30]
    pix = PeriodIndex(result.index.values, freq='H')
    mask = (pix >= lb) & (pix < ub)
    rs = result[mask]
    assert (rs == ts[lb]).all()
    ts[5:10] = np.nan
    ts[15:20] = np.nan
    val1 = ts.asof(ts.index[7])
    val2 = ts.asof(ts.index[19])
    assert val1 == ts[4]
    assert val2 == ts[14]
    val1 = ts.asof(str(ts.index[7]))
    assert val1 == ts[4]
    assert ts.asof(ts.index[3]) == ts[3]
    d = ts.index[0].to_timestamp() - offsets.BDay()
    assert isna(ts.asof(d))