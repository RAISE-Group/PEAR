def test_date_range_timestamp_equiv_explicit_pytz(self):
    rng = date_range('20090415', '20090519', tz=pytz.timezone('US/Eastern'))
    stamp = rng[0]
    ts = Timestamp('20090415', tz=pytz.timezone('US/Eastern'), freq='D')
    assert ts == stamp