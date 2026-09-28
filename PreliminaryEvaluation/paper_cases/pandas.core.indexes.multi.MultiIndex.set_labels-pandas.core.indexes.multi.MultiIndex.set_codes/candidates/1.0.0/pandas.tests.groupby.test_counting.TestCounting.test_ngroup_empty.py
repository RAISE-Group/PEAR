def test_ngroup_empty(self):
    ge = DataFrame().groupby(level=0)
    se = Series(dtype=object).groupby(level=0)
    e = Series(dtype='int64')
    tm.assert_series_equal(e, ge.ngroup())
    tm.assert_series_equal(e, se.ngroup())