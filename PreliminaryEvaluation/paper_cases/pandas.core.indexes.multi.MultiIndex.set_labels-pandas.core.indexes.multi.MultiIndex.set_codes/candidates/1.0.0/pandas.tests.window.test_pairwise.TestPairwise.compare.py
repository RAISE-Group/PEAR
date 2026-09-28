def compare(self, result, expected):
    result = result.dropna().values
    expected = expected.dropna().values
    tm.assert_numpy_array_equal(result, expected, check_dtype=False)