def test_ctor_str_intraday(self):
    rng = DatetimeIndex(['1-1-2000 00:00:01'])
    assert rng[0].second == 1