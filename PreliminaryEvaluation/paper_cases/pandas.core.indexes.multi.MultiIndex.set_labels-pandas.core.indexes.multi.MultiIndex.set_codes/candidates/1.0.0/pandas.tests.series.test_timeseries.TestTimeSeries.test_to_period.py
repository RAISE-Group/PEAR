def test_to_period(self):
    from pandas.core.indexes.period import period_range
    ts = _simple_ts('1/1/2000', '1/1/2001')
    pts = ts.to_period()
    exp = ts.copy()
    exp.index = period_range('1/1/2000', '1/1/2001')
    tm.assert_series_equal(pts, exp)
    pts = ts.to_period('M')
    exp.index = exp.index.asfreq('M')
    tm.assert_index_equal(pts.index, exp.index.asfreq('M'))
    tm.assert_series_equal(pts, exp)
    idx = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'])
    exp_idx = pd.PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], freq='D')
    s = Series(np.random.randn(4), index=idx)
    expected = s.copy()
    expected.index = exp_idx
    tm.assert_series_equal(s.to_period(), expected)
    df = DataFrame(np.random.randn(4, 4), index=idx, columns=idx)
    expected = df.copy()
    expected.index = exp_idx
    tm.assert_frame_equal(df.to_period(), expected)
    expected = df.copy()
    expected.columns = exp_idx
    tm.assert_frame_equal(df.to_period(axis=1), expected)