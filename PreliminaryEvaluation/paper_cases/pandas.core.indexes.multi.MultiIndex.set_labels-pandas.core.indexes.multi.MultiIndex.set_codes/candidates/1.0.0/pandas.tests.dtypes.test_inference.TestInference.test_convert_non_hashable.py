def test_convert_non_hashable(self):
    arr = np.array([[10.0, 2], 1.0, 'apple'], dtype=object)
    result = lib.maybe_convert_numeric(arr, set(), False, True)
    tm.assert_numpy_array_equal(result, np.array([np.nan, 1.0, np.nan]))