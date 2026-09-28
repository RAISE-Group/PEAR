def test_contains(self, interval):
    assert 0.5 in interval
    assert 1 in interval
    assert 0 not in interval
    msg = '__contains__ not defined for two intervals'
    with pytest.raises(TypeError, match=msg):
        interval in interval
    interval_both = Interval(0, 1, closed='both')
    assert 0 in interval_both
    assert 1 in interval_both
    interval_neither = Interval(0, 1, closed='neither')
    assert 0 not in interval_neither
    assert 0.5 in interval_neither
    assert 1 not in interval_neither