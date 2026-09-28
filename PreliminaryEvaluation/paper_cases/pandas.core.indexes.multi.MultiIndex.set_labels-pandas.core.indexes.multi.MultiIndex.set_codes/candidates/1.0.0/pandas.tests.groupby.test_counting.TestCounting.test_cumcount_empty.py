def test_cumcount_empty(self):
    ge = DataFrame().groupby(level=0)
    se = Series(dtype=object).groupby(level=0)
    e = Series(dtype='int64')
    tm.assert_series_equal(e, ge.cumcount())
    tm.assert_series_equal(e, se.cumcount())