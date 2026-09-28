@pytest.mark.parametrize('left, right, op, expected', [([True, False, np.nan], [True, False, True], operator.and_, [True, False, False]), ([True, False, True], [True, False, np.nan], operator.and_, [True, False, False]), ([True, False, np.nan], [True, False, True], operator.or_, [True, False, False]), ([True, False, True], [True, False, np.nan], operator.or_, [True, False, True])])
def test_logical_operators_nans(self, left, right, op, expected):
    result = op(DataFrame(left), DataFrame(right))
    expected = DataFrame(expected)
    tm.assert_frame_equal(result, expected)