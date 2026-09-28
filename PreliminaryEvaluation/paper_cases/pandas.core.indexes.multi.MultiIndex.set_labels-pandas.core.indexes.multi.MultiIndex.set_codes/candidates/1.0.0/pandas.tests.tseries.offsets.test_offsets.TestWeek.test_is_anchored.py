def test_is_anchored(self):
    assert Week(weekday=0).is_anchored()
    assert not Week().is_anchored()
    assert not Week(2, weekday=2).is_anchored()
    assert not Week(2).is_anchored()