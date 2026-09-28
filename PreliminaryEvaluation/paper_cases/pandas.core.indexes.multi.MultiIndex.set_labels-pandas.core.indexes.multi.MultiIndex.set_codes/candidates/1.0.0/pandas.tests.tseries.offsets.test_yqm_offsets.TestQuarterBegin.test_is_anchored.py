def test_is_anchored(self):
    assert QuarterBegin(startingMonth=1).is_anchored()
    assert QuarterBegin().is_anchored()
    assert not QuarterBegin(2, startingMonth=1).is_anchored()