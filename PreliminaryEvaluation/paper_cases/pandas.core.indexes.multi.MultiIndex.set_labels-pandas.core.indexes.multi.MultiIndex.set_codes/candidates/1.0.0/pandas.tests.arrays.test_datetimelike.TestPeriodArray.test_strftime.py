def test_strftime(self, period_index):
    arr = PeriodArray(period_index)
    result = arr.strftime('%Y')
    expected = np.array([per.strftime('%Y') for per in arr], dtype=object)
    tm.assert_numpy_array_equal(result, expected)