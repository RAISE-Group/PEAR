def test_is_anchored(self):
    assert BQuarterEnd(startingMonth=1).is_anchored()
    assert BQuarterEnd().is_anchored()
    assert not BQuarterEnd(2, startingMonth=1).is_anchored()