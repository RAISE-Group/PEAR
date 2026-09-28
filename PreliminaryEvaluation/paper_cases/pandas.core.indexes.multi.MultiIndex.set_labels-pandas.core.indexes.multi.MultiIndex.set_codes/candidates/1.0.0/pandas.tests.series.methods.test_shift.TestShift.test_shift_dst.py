def test_shift_dst(self):
    dates = date_range('2016-11-06', freq='H', periods=10, tz='US/Eastern')
    s = Series(dates)
    res = s.shift(0)
    tm.assert_series_equal(res, s)
    assert res.dtype == 'datetime64[ns, US/Eastern]'
    res = s.shift(1)
    exp_vals = [NaT] + dates.astype(object).values.tolist()[:9]
    exp = Series(exp_vals)
    tm.assert_series_equal(res, exp)
    assert res.dtype == 'datetime64[ns, US/Eastern]'
    res = s.shift(-2)
    exp_vals = dates.astype(object).values.tolist()[2:] + [NaT, NaT]
    exp = Series(exp_vals)
    tm.assert_series_equal(res, exp)
    assert res.dtype == 'datetime64[ns, US/Eastern]'
    for ex in [10, -10, 20, -20]:
        res = s.shift(ex)
        exp = Series([NaT] * 10, dtype='datetime64[ns, US/Eastern]')
        tm.assert_series_equal(res, exp)
        assert res.dtype == 'datetime64[ns, US/Eastern]'