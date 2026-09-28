def test_range_closed_with_tz_aware_start_end(self):
    begin = Timestamp('2011/1/1', tz='US/Eastern')
    end = Timestamp('2014/1/1', tz='US/Eastern')
    for freq in ['1D', '3D', '2M', '7W', '3H', 'A']:
        closed = date_range(begin, end, closed=None, freq=freq)
        left = date_range(begin, end, closed='left', freq=freq)
        right = date_range(begin, end, closed='right', freq=freq)
        expected_left = left
        expected_right = right
        if end == closed[-1]:
            expected_left = closed[:-1]
        if begin == closed[0]:
            expected_right = closed[1:]
        tm.assert_index_equal(expected_left, left)
        tm.assert_index_equal(expected_right, right)
    begin = Timestamp('2011/1/1')
    end = Timestamp('2014/1/1')
    begintz = Timestamp('2011/1/1', tz='US/Eastern')
    endtz = Timestamp('2014/1/1', tz='US/Eastern')
    for freq in ['1D', '3D', '2M', '7W', '3H', 'A']:
        closed = date_range(begin, end, closed=None, freq=freq, tz='US/Eastern')
        left = date_range(begin, end, closed='left', freq=freq, tz='US/Eastern')
        right = date_range(begin, end, closed='right', freq=freq, tz='US/Eastern')
        expected_left = left
        expected_right = right
        if endtz == closed[-1]:
            expected_left = closed[:-1]
        if begintz == closed[0]:
            expected_right = closed[1:]
        tm.assert_index_equal(expected_left, left)
        tm.assert_index_equal(expected_right, right)