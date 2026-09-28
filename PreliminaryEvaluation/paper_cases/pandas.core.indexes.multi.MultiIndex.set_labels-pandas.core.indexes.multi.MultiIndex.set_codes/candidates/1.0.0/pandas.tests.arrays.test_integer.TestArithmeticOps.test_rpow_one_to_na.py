def test_rpow_one_to_na(self):
    arr = integer_array([np.nan, np.nan])
    result = np.array([1.0, 2.0]) ** arr
    expected = np.array([1.0, np.nan])
    tm.assert_numpy_array_equal(result, expected)