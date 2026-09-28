def test_is_anchored(self):
    assert QuarterEnd(startingMonth=1).is_anchored()
    assert QuarterEnd().is_anchored()
    assert not QuarterEnd(2, startingMonth=1).is_anchored()