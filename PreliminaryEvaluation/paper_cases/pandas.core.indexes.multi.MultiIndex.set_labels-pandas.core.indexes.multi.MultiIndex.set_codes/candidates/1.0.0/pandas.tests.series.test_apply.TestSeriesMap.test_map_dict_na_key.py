def test_map_dict_na_key(self):
    s = Series([1, 2, np.nan])
    expected = Series(['a', 'b', 'c'])
    result = s.map({1: 'a', 2: 'b', np.nan: 'c'})
    tm.assert_series_equal(result, expected)