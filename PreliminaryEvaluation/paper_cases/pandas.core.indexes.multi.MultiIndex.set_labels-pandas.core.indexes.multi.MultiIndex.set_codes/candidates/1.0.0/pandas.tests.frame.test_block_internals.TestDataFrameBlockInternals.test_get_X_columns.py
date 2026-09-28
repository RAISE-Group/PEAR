def test_get_X_columns(self):
    df = DataFrame({'a': [1, 2, 3], 'b': [True, False, True], 'c': ['foo', 'bar', 'baz'], 'd': [None, None, None], 'e': [3.14, 0.577, 2.773]})
    tm.assert_index_equal(df._get_numeric_data().columns, pd.Index(['a', 'b', 'e']))