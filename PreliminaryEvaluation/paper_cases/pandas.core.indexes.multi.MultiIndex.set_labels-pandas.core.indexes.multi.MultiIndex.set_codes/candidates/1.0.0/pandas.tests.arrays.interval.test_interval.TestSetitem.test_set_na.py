def test_set_na(self, left_right_dtypes):
    left, right = left_right_dtypes
    result = IntervalArray.from_arrays(left, right)
    result[0] = np.nan
    expected_left = Index([left._na_value] + list(left[1:]))
    expected_right = Index([right._na_value] + list(right[1:]))
    expected = IntervalArray.from_arrays(expected_left, expected_right)
    tm.assert_extension_array_equal(result, expected)