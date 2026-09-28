def test_map_abc_mapping_with_missing(self, non_mapping_dict_subclass):

    class NonDictMappingWithMissing(non_mapping_dict_subclass):

        def __missing__(self, key):
            return 'missing'
    s = Series([1, 2, 3])
    not_a_dictionary = NonDictMappingWithMissing({3: 'three'})
    result = s.map(not_a_dictionary)
    expected = Series([np.nan, np.nan, 'three'])
    tm.assert_series_equal(result, expected)