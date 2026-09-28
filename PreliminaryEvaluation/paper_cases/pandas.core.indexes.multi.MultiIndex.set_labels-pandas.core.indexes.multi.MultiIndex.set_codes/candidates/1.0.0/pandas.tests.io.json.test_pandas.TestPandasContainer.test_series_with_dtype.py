def test_series_with_dtype(self):
    s = Series([4.56, 4.56, 4.56])
    result = read_json(s.to_json(), typ='series', dtype=np.int64)
    expected = Series([4] * 3)
    tm.assert_series_equal(result, expected)