def test_tz_conversion_freq(self, tz_naive_fixture):
    t1 = Timestamp('2019-01-01 10:00', freq='H')
    assert t1.tz_localize(tz=tz_naive_fixture).freq == t1.freq
    t2 = Timestamp('2019-01-02 12:00', tz='UTC', freq='T')
    assert t2.tz_convert(tz='UTC').freq == t2.freq