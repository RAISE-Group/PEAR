@pytest.mark.parametrize('left, right, op, expected', [([True, False, np.nan], [True, False, True], operator.and_, [True, False, False]), ([True, False, True], [True, False, np.nan], operator.and_, [True, False, False]), ([True, False, np.nan], [True, False, True], operator.or_, [True, False, False]), ([True, False, True], [True, False, np.nan], operator.or_, [True, False, True])])
def test_logical_operators_nans(self, left, right, op, expected):
    result = op(Series(left), Series(right))
    expected = Series(expected)
    tm.assert_series_equal(result, expected)