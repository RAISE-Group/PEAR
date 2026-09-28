def test_tolerance_float(self):
    left = pd.DataFrame({'a': [1.1, 3.5, 10.9], 'left_val': ['a', 'b', 'c']})
    right = pd.DataFrame({'a': [1.0, 2.5, 3.3, 7.5, 11.5], 'right_val': [1.0, 2.5, 3.3, 7.5, 11.5]})
    expected = pd.DataFrame({'a': [1.1, 3.5, 10.9], 'left_val': ['a', 'b', 'c'], 'right_val': [1, 3.3, np.nan]})
    result = pd.merge_asof(left, right, on='a', direction='nearest', tolerance=0.5)
    tm.assert_frame_equal(result, expected)