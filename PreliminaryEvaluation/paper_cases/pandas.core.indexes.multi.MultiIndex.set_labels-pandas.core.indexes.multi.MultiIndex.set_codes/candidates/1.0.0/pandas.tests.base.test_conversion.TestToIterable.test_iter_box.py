def test_iter_box(self):
    vals = [Timestamp('2011-01-01'), Timestamp('2011-01-02')]
    s = Series(vals)
    assert s.dtype == 'datetime64[ns]'
    for res, exp in zip(s, vals):
        assert isinstance(res, Timestamp)
        assert res.tz is None
        assert res == exp
    vals = [Timestamp('2011-01-01', tz='US/Eastern'), Timestamp('2011-01-02', tz='US/Eastern')]
    s = Series(vals)
    assert s.dtype == 'datetime64[ns, US/Eastern]'
    for res, exp in zip(s, vals):
        assert isinstance(res, Timestamp)
        assert res.tz == exp.tz
        assert res == exp
    vals = [Timedelta('1 days'), Timedelta('2 days')]
    s = Series(vals)
    assert s.dtype == 'timedelta64[ns]'
    for res, exp in zip(s, vals):
        assert isinstance(res, Timedelta)
        assert res == exp
    vals = [pd.Period('2011-01-01', freq='M'), pd.Period('2011-01-02', freq='M')]
    s = Series(vals)
    assert s.dtype == 'Period[M]'
    for res, exp in zip(s, vals):
        assert isinstance(res, pd.Period)
        assert res.freq == 'M'
        assert res == exp