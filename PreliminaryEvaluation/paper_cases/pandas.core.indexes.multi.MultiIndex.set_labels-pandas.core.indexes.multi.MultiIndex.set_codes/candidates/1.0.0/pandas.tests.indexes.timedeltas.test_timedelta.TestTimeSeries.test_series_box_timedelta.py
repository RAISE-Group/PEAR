def test_series_box_timedelta(self):
    rng = timedelta_range('1 day 1 s', periods=5, freq='h')
    s = Series(rng)
    assert isinstance(s[1], Timedelta)
    assert isinstance(s.iat[2], Timedelta)