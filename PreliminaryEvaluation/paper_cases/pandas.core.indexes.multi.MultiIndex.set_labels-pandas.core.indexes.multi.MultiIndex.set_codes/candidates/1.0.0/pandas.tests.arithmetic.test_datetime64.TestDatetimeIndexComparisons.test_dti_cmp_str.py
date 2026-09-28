def test_dti_cmp_str(self, tz_naive_fixture):
    tz = tz_naive_fixture
    rng = date_range('1/1/2000', periods=10, tz=tz)
    other = '1/1/2000'
    result = rng == other
    expected = np.array([True] + [False] * 9)
    tm.assert_numpy_array_equal(result, expected)
    result = rng != other
    expected = np.array([False] + [True] * 9)
    tm.assert_numpy_array_equal(result, expected)
    result = rng < other
    expected = np.array([False] * 10)
    tm.assert_numpy_array_equal(result, expected)
    result = rng <= other
    expected = np.array([True] + [False] * 9)
    tm.assert_numpy_array_equal(result, expected)
    result = rng > other
    expected = np.array([False] + [True] * 9)
    tm.assert_numpy_array_equal(result, expected)
    result = rng >= other
    expected = np.array([True] * 10)
    tm.assert_numpy_array_equal(result, expected)