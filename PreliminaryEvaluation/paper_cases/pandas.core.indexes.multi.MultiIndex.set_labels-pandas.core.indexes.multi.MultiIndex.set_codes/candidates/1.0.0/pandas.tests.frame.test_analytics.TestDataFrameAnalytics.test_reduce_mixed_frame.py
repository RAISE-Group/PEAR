def test_reduce_mixed_frame(self):
    df = DataFrame({'bool_data': [True, True, False, False, False], 'int_data': [10, 20, 30, 40, 50], 'string_data': ['a', 'b', 'c', 'd', 'e']})
    df.reindex(columns=['bool_data', 'int_data', 'string_data'])
    test = df.sum(axis=0)
    tm.assert_numpy_array_equal(test.values, np.array([2, 150, 'abcde'], dtype=object))
    tm.assert_series_equal(test, df.T.sum(axis=1))