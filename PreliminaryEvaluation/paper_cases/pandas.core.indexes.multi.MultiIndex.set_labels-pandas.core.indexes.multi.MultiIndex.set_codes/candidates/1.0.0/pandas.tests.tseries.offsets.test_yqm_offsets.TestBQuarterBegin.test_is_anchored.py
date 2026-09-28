def test_is_anchored(self):
    assert BQuarterBegin(startingMonth=1).is_anchored()
    assert BQuarterBegin().is_anchored()
    assert not BQuarterBegin(2, startingMonth=1).is_anchored()