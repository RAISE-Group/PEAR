def test_equal(self):
    assert Interval(0, 1) == Interval(0, 1, closed='right')
    assert Interval(0, 1) != Interval(0, 1, closed='left')
    assert Interval(0, 1) != 0