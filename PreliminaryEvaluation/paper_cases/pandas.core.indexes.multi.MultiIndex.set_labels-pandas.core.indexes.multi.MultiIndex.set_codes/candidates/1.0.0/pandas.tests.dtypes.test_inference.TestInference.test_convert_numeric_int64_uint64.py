@pytest.mark.parametrize('case', [np.array([2 ** 63, -1], dtype=object), np.array([str(2 ** 63), -1], dtype=object), np.array([str(2 ** 63), str(-1)], dtype=object), np.array([-1, 2 ** 63], dtype=object), np.array([-1, str(2 ** 63)], dtype=object), np.array([str(-1), str(2 ** 63)], dtype=object)])
def test_convert_numeric_int64_uint64(self, case, coerce):
    expected = case.astype(float) if coerce else case.copy()
    result = lib.maybe_convert_numeric(case, set(), coerce_numeric=coerce)
    tm.assert_almost_equal(result, expected)