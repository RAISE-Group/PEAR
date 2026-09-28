def test_parr_cmp_period_scalar2(self, box_with_array):
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    pi = pd.period_range('2000-01-01', periods=10, freq='D')
    val = Period('2000-01-04', freq='D')
    expected = [x > val for x in pi]
    ser = tm.box_expected(pi, box_with_array)
    expected = tm.box_expected(expected, xbox)
    result = ser > val
    tm.assert_equal(result, expected)
    val = pi[5]
    result = ser > val
    expected = [x > val for x in pi]
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)