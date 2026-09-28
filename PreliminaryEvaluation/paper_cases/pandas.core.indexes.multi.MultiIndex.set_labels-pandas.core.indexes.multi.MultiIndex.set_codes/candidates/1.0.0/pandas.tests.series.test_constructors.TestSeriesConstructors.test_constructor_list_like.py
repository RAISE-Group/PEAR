def test_constructor_list_like(self):
    expected = Series([1, 2, 3], dtype='int64')
    for obj in [[1, 2, 3], (1, 2, 3), np.array([1, 2, 3], dtype='int64')]:
        result = Series(obj, index=[0, 1, 2])
        tm.assert_series_equal(result, expected)