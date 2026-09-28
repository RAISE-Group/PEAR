def test_constructor_mapping(self, non_mapping_dict_subclass):
    ndm = non_mapping_dict_subclass({3: 'three'})
    result = Series(ndm)
    expected = Series(['three'], index=[3])
    tm.assert_series_equal(result, expected)