def test_all_any(self):
    ts = tm.makeTimeSeries()
    bool_series = ts > 0
    assert not bool_series.all()
    assert bool_series.any()
    s = Series(['abc', True])
    assert 'abc' == s.any()