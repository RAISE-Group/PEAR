def test_fill_value_when_combine_const(self):
    s = Series([0, 1, np.nan, 3, 4, 5])
    exp = s.fillna(0).add(2)
    res = s.add(2, fill_value=0)
    tm.assert_series_equal(res, exp)