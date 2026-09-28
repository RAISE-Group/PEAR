def test_constructor_int_dtype_nan(self):
    data = [np.nan]
    expected = Float64Index(data)
    result = Index(data, dtype='float')
    tm.assert_index_equal(result, expected)