@pytest.mark.parametrize('arr', [np.array([2 ** 63, np.nan], dtype=object), np.array([str(2 ** 63), np.nan], dtype=object), np.array([np.nan, 2 ** 63], dtype=object), np.array([np.nan, str(2 ** 63)], dtype=object)])
def test_convert_numeric_uint64_nan(self, coerce, arr):
    expected = arr.astype(float) if coerce else arr.copy()
    result = lib.maybe_convert_numeric(arr, set(), coerce_numeric=coerce)
    tm.assert_almost_equal(result, expected)