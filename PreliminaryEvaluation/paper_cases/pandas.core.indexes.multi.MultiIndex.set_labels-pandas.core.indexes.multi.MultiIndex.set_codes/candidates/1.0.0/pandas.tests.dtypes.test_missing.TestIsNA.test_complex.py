@pytest.mark.parametrize('value, expected', [(np.complex128(np.nan), True), (np.float64(1), False), (np.array([1, 1 + 0j, np.nan, 3]), np.array([False, False, True, False])), (np.array([1, 1 + 0j, np.nan, 3], dtype=object), np.array([False, False, True, False])), (np.array([1, 1 + 0j, np.nan, 3]).astype(object), np.array([False, False, True, False]))])
def test_complex(self, value, expected):
    result = isna(value)
    if is_scalar(result):
        assert result is expected
    else:
        tm.assert_numpy_array_equal(result, expected)