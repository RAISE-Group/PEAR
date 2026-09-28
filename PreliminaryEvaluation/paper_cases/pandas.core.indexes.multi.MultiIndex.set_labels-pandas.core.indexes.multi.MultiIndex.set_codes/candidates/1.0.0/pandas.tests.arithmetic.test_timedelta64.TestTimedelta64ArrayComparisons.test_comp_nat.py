@pytest.mark.parametrize('dtype', [None, object])
def test_comp_nat(self, dtype):
    left = pd.TimedeltaIndex([pd.Timedelta('1 days'), pd.NaT, pd.Timedelta('3 days')])
    right = pd.TimedeltaIndex([pd.NaT, pd.NaT, pd.Timedelta('3 days')])
    lhs, rhs = (left, right)
    if dtype is object:
        lhs, rhs = (left.astype(object), right.astype(object))
    result = rhs == lhs
    expected = np.array([False, False, True])
    tm.assert_numpy_array_equal(result, expected)
    result = rhs != lhs
    expected = np.array([True, True, False])
    tm.assert_numpy_array_equal(result, expected)
    expected = np.array([False, False, False])
    tm.assert_numpy_array_equal(lhs == pd.NaT, expected)
    tm.assert_numpy_array_equal(pd.NaT == rhs, expected)
    expected = np.array([True, True, True])
    tm.assert_numpy_array_equal(lhs != pd.NaT, expected)
    tm.assert_numpy_array_equal(pd.NaT != lhs, expected)
    expected = np.array([False, False, False])
    tm.assert_numpy_array_equal(lhs < pd.NaT, expected)
    tm.assert_numpy_array_equal(pd.NaT > lhs, expected)