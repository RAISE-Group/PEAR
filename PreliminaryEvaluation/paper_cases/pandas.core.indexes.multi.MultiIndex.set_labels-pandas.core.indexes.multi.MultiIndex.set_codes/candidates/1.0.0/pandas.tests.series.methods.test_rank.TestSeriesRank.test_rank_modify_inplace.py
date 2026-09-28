def test_rank_modify_inplace(self):
    s = Series([Timestamp('2017-01-05 10:20:27.569000'), NaT])
    expected = s.copy()
    s.rank()
    result = s
    tm.assert_series_equal(result, expected)