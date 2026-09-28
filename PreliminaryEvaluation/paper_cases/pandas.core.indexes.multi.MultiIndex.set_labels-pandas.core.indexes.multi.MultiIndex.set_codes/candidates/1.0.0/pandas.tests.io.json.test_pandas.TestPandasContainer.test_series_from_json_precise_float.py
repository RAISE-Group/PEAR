def test_series_from_json_precise_float(self):
    s = Series([4.56, 4.56, 4.56])
    result = read_json(s.to_json(), typ='series', precise_float=True)
    tm.assert_series_equal(result, s, check_index_type=False)