def test_map_na_exclusion(self):
    index = Index([1.5, np.nan, 3, np.nan, 5])
    result = index.map(lambda x: x * 2, na_action='ignore')
    expected = index * 2
    tm.assert_index_equal(result, expected)