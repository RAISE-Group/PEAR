def test_make_time_series(self):
    index = period_range(freq='A', start='1/1/2001', end='12/1/2009')
    series = Series(1, index=index)
    assert isinstance(series, Series)