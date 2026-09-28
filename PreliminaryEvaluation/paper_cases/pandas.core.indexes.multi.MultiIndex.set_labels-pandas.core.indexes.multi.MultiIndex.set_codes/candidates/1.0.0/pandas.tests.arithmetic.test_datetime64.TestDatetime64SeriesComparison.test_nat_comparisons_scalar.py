@pytest.mark.parametrize('data', [[Timestamp('2011-01-01'), NaT, Timestamp('2011-01-03')], [Timedelta('1 days'), NaT, Timedelta('3 days')], [Period('2011-01', freq='M'), NaT, Period('2011-03', freq='M')]])
@pytest.mark.parametrize('dtype', [None, object])
def test_nat_comparisons_scalar(self, dtype, data, box_with_array):
    if box_with_array is tm.to_array and dtype is object:
        return
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    left = Series(data, dtype=dtype)
    left = tm.box_expected(left, box_with_array)
    expected = [False, False, False]
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(left == NaT, expected)
    tm.assert_equal(NaT == left, expected)
    expected = [True, True, True]
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(left != NaT, expected)
    tm.assert_equal(NaT != left, expected)
    expected = [False, False, False]
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(left < NaT, expected)
    tm.assert_equal(NaT > left, expected)
    tm.assert_equal(left <= NaT, expected)
    tm.assert_equal(NaT >= left, expected)
    tm.assert_equal(left > NaT, expected)
    tm.assert_equal(NaT < left, expected)
    tm.assert_equal(left >= NaT, expected)
    tm.assert_equal(NaT <= left, expected)