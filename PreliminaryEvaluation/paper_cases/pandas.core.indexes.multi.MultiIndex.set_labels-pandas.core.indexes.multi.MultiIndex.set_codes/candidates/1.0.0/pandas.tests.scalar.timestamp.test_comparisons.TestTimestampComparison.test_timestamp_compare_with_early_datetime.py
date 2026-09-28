def test_timestamp_compare_with_early_datetime(self):
    stamp = Timestamp('2012-01-01')
    assert not stamp == datetime.min
    assert not stamp == datetime(1600, 1, 1)
    assert not stamp == datetime(2700, 1, 1)
    assert stamp != datetime.min
    assert stamp != datetime(1600, 1, 1)
    assert stamp != datetime(2700, 1, 1)
    assert stamp > datetime(1600, 1, 1)
    assert stamp >= datetime(1600, 1, 1)
    assert stamp < datetime(2700, 1, 1)
    assert stamp <= datetime(2700, 1, 1)