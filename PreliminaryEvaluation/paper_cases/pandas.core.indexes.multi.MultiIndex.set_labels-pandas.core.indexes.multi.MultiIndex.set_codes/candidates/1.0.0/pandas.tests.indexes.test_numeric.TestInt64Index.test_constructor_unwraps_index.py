def test_constructor_unwraps_index(self):
    idx = pd.Index([1, 2])
    result = pd.Int64Index(idx)
    expected = np.array([1, 2], dtype='int64')
    tm.assert_numpy_array_equal(result._data, expected)