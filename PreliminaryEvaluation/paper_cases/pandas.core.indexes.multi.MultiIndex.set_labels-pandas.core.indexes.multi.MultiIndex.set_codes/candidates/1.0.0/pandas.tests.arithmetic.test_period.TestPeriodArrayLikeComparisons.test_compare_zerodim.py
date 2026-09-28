def test_compare_zerodim(self, box_with_array):
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    pi = pd.period_range('2000', periods=4)
    other = np.array(pi.to_numpy()[0])
    pi = tm.box_expected(pi, box_with_array)
    result = pi <= other
    expected = np.array([True, False, False, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)