def test_pi_add_offset_n_gt1_not_divisible(self, box_with_array):
    pi = pd.PeriodIndex(['2016-01'], freq='2M')
    expected = pd.PeriodIndex(['2016-04'], freq='2M')
    pi = tm.box_expected(pi, box_with_array, transpose=False)
    expected = tm.box_expected(expected, box_with_array, transpose=False)
    result = pi + to_offset('3M')
    tm.assert_equal(result, expected)
    result = to_offset('3M') + pi
    tm.assert_equal(result, expected)