def test_convert_numeric_uint64_nan_values(self, coerce):
    arr = np.array([2 ** 63, 2 ** 63 + 1], dtype=object)
    na_values = {2 ** 63}
    expected = np.array([np.nan, 2 ** 63 + 1], dtype=float) if coerce else arr.copy()
    result = lib.maybe_convert_numeric(arr, na_values, coerce_numeric=coerce)
    tm.assert_almost_equal(result, expected)