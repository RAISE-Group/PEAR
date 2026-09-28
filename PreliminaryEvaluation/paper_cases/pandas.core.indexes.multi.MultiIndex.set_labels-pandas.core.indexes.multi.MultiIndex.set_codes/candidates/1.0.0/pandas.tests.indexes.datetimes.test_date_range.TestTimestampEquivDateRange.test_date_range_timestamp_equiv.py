def test_date_range_timestamp_equiv(self):
    rng = date_range('20090415', '20090519', tz='US/Eastern')
    stamp = rng[0]
    ts = Timestamp('20090415', tz='US/Eastern', freq='D')
    assert ts == stamp