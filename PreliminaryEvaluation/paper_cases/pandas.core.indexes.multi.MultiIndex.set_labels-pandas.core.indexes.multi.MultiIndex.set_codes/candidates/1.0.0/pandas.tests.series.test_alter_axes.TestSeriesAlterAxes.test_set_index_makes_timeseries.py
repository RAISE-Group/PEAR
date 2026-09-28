def test_set_index_makes_timeseries(self):
    idx = tm.makeDateIndex(10)
    s = Series(range(10))
    s.index = idx
    assert s.index.is_all_dates