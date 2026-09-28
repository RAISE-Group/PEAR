def test_cached_range_bug(self):
    rng = date_range('2010-09-01 05:00:00', periods=50, freq=DateOffset(hours=6))
    assert len(rng) == 50
    assert rng[0] == datetime(2010, 9, 1, 5)