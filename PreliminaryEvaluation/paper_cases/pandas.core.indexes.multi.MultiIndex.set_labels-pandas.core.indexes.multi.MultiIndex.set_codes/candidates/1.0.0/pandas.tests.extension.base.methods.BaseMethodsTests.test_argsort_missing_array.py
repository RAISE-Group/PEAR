def test_argsort_missing_array(self, data_missing_for_sorting):
    result = data_missing_for_sorting.argsort()
    expected = np.array([2, 0, 1], dtype=np.dtype('int'))
    result = result.astype('int64', casting='safe')
    expected = expected.astype('int64', casting='safe')
    tm.assert_numpy_array_equal(result, expected)