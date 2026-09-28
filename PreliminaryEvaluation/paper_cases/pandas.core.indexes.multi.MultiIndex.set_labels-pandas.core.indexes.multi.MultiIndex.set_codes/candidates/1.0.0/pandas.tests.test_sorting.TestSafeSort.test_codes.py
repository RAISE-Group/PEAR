@pytest.mark.parametrize('verify', [True, False])
def test_codes(self, verify):
    values = [3, 1, 2, 0, 4]
    expected = np.array([0, 1, 2, 3, 4])
    codes = [0, 1, 1, 2, 3, 0, -1, 4]
    result, result_codes = safe_sort(values, codes, verify=verify)
    expected_codes = np.array([3, 1, 1, 2, 0, 3, -1, 4], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    tm.assert_numpy_array_equal(result_codes, expected_codes)
    codes = [0, 1, 1, 2, 3, 0, 99, 4]
    result, result_codes = safe_sort(values, codes, na_sentinel=99, verify=verify)
    expected_codes = np.array([3, 1, 1, 2, 0, 3, 99, 4], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    tm.assert_numpy_array_equal(result_codes, expected_codes)
    codes = []
    result, result_codes = safe_sort(values, codes, verify=verify)
    expected_codes = np.array([], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    tm.assert_numpy_array_equal(result_codes, expected_codes)