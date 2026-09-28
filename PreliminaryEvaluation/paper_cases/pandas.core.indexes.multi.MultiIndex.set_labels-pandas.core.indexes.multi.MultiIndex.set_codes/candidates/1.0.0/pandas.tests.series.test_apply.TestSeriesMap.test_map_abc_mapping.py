def test_map_abc_mapping(self, non_mapping_dict_subclass):
    s = Series([1, 2, 3])
    not_a_dictionary = non_mapping_dict_subclass({3: 'three'})
    result = s.map(not_a_dictionary)
    expected = Series([np.nan, np.nan, 'three'])
    tm.assert_series_equal(result, expected)