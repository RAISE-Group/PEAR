def test_date_range_timestamp_equiv_dateutil(self):
    rng = date_range('20090415', '20090519', tz='dateutil/US/Eastern')
    stamp = rng[0]
    ts = Timestamp('20090415', tz='dateutil/US/Eastern', freq='D')
    assert ts == stamp