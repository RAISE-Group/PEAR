def test_any_all_bool_only(self):
    df = DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [None, None, None]})
    result = df.all(bool_only=True)
    expected = Series(dtype=np.bool)
    tm.assert_series_equal(result, expected)
    df = DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [None, None, None], 'col4': [False, False, True]})
    result = df.all(bool_only=True)
    expected = Series({'col4': False})
    tm.assert_series_equal(result, expected)