@pytest.mark.parametrize('closed', ['right', 'left', None])
def test_range_closed_boundary(self, closed):
    right_boundary = date_range('2015-09-12', '2015-12-01', freq='QS-MAR', closed=closed)
    left_boundary = date_range('2015-09-01', '2015-09-12', freq='QS-MAR', closed=closed)
    both_boundary = date_range('2015-09-01', '2015-12-01', freq='QS-MAR', closed=closed)
    expected_right = expected_left = expected_both = both_boundary
    if closed == 'right':
        expected_left = both_boundary[1:]
    if closed == 'left':
        expected_right = both_boundary[:-1]
    if closed is None:
        expected_right = both_boundary[1:]
        expected_left = both_boundary[:-1]
    tm.assert_index_equal(right_boundary, expected_right)
    tm.assert_index_equal(left_boundary, expected_left)
    tm.assert_index_equal(both_boundary, expected_both)