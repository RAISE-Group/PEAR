def test_convert_preserve_all_bool(self):
    s = Series([False, True, False, False], dtype=object)
    r = s._convert(datetime=True, numeric=True)
    e = Series([False, True, False, False], dtype=bool)
    tm.assert_series_equal(r, e)