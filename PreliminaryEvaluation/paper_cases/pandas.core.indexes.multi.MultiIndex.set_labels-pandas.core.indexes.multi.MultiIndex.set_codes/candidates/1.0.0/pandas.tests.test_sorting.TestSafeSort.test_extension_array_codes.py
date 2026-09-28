@pytest.mark.parametrize('verify', [True, False])
@pytest.mark.parametrize('na_sentinel', [-1, 99])
def test_extension_array_codes(self, verify, na_sentinel):
    a = array([1, 3, 2], dtype='Int64')
    result, codes = safe_sort(a, [0, 1, na_sentinel, 2], na_sentinel=na_sentinel, verify=verify)
    expected_values = array([1, 2, 3], dtype='Int64')
    expected_codes = np.array([0, 2, na_sentinel, 1], dtype=np.intp)
    tm.assert_extension_array_equal(result, expected_values)
    tm.assert_numpy_array_equal(codes, expected_codes)