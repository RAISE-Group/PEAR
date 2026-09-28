def test_overlaps_nested(self, start_shift, closed, other_closed):
    start, shift = start_shift
    interval1 = Interval(start, start + 3 * shift, other_closed)
    interval2 = Interval(start + shift, start + 2 * shift, closed)
    assert interval1.overlaps(interval2)