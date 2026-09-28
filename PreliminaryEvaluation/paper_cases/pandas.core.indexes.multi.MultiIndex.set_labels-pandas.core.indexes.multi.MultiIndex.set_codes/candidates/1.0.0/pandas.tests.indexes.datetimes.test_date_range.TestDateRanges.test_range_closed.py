@pytest.mark.parametrize('freq', ['1D', '3D', '2M', '7W', '3H', 'A'])
def test_range_closed(self, freq):
    begin = datetime(2011, 1, 1)
    end = datetime(2014, 1, 1)
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