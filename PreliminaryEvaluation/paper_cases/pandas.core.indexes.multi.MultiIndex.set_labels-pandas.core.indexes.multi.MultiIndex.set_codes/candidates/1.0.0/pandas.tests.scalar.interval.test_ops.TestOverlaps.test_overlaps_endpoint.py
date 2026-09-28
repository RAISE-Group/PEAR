def test_overlaps_endpoint(self, start_shift, closed, other_closed):
    start, shift = start_shift
    interval1 = Interval(start, start + shift, other_closed)
    interval2 = Interval(start + shift, start + 2 * shift, closed)
    result = interval1.overlaps(interval2)
    expected = interval1.closed_right and interval2.closed_left
    assert result == expected