def test_convert_preserve_bool(self):
    s = Series([1, True, 3, 5], dtype=object)
    r = s._convert(datetime=True, numeric=True)
    e = Series([1, 1, 3, 5], dtype='i8')
    tm.assert_series_equal(r, e)