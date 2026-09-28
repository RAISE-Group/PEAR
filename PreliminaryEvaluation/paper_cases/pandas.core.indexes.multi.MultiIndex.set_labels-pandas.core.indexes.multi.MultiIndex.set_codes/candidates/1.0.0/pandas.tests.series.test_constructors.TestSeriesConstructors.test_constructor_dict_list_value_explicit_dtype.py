def test_constructor_dict_list_value_explicit_dtype(self):
    d = {'a': [[2], [3], [4]]}
    result = Series(d, index=['a'], dtype='object')
    expected = Series(d, index=['a'])
    tm.assert_series_equal(result, expected)