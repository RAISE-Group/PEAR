@pytest.mark.parametrize('na_sentinel', [-1, 99])
def test_codes_out_of_bound(self, na_sentinel):
    values = [3, 1, 2, 0, 4]
    expected = np.array([0, 1, 2, 3, 4])
    codes = [0, 101, 102, 2, 3, 0, 99, 4]
    result, result_codes = safe_sort(values, codes, na_sentinel=na_sentinel)
    expected_codes = np.array([3, na_sentinel, na_sentinel, 2, 0, 3, na_sentinel, 4], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    tm.assert_numpy_array_equal(result_codes, expected_codes)