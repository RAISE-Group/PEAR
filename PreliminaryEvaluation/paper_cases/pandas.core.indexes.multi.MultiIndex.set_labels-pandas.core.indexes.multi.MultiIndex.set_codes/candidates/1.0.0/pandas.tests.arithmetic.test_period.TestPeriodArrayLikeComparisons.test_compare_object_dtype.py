@pytest.mark.parametrize('other_box', [list, np.array, lambda x: x.astype(object)])
def test_compare_object_dtype(self, box_with_array, other_box):
    pi = pd.period_range('2000', periods=5)
    parr = tm.box_expected(pi, box_with_array)
    xbox = np.ndarray if box_with_array is pd.Index else box_with_array
    other = other_box(pi)
    expected = np.array([True, True, True, True, True])
    expected = tm.box_expected(expected, xbox)
    result = parr == other
    tm.assert_equal(result, expected)
    result = parr <= other
    tm.assert_equal(result, expected)
    result = parr >= other
    tm.assert_equal(result, expected)
    result = parr != other
    tm.assert_equal(result, ~expected)
    result = parr < other
    tm.assert_equal(result, ~expected)
    result = parr > other
    tm.assert_equal(result, ~expected)
    other = other_box(pi[::-1])
    expected = np.array([False, False, True, False, False])
    expected = tm.box_expected(expected, xbox)
    result = parr == other
    tm.assert_equal(result, expected)
    expected = np.array([True, True, True, False, False])
    expected = tm.box_expected(expected, xbox)
    result = parr <= other
    tm.assert_equal(result, expected)
    expected = np.array([False, False, True, True, True])
    expected = tm.box_expected(expected, xbox)
    result = parr >= other
    tm.assert_equal(result, expected)
    expected = np.array([True, True, False, True, True])
    expected = tm.box_expected(expected, xbox)
    result = parr != other
    tm.assert_equal(result, expected)
    expected = np.array([True, True, False, False, False])
    expected = tm.box_expected(expected, xbox)
    result = parr < other
    tm.assert_equal(result, expected)
    expected = np.array([False, False, False, True, True])
    expected = tm.box_expected(expected, xbox)
    result = parr > other
    tm.assert_equal(result, expected)