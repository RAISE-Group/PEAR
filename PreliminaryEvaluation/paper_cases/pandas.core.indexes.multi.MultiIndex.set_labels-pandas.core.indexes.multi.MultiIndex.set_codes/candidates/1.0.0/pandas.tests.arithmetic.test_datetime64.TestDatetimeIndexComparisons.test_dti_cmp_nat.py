@pytest.mark.parametrize('dtype', [None, object])
def test_dti_cmp_nat(self, dtype, box_with_array):
    if box_with_array is tm.to_array and dtype is object:
        return
    xbox = box_with_array if box_with_array is not pd.Index else np.ndarray
    left = pd.DatetimeIndex([pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2011-01-03')])
    right = pd.DatetimeIndex([pd.NaT, pd.NaT, pd.Timestamp('2011-01-03')])
    left = tm.box_expected(left, box_with_array)
    right = tm.box_expected(right, box_with_array)
    lhs, rhs = (left, right)
    if dtype is object:
        lhs, rhs = (left.astype(object), right.astype(object))
    result = rhs == lhs
    expected = np.array([False, False, True])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)
    result = lhs != rhs
    expected = np.array([True, True, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(result, expected)
    expected = np.array([False, False, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(lhs == pd.NaT, expected)
    tm.assert_equal(pd.NaT == rhs, expected)
    expected = np.array([True, True, True])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(lhs != pd.NaT, expected)
    tm.assert_equal(pd.NaT != lhs, expected)
    expected = np.array([False, False, False])
    expected = tm.box_expected(expected, xbox)
    tm.assert_equal(lhs < pd.NaT, expected)
    tm.assert_equal(pd.NaT > lhs, expected)