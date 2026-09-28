@pytest.mark.parametrize('tzstr', ['Europe/Brussels', 'Asia/Tokyo', 'US/Pacific'])
def test_to_timestamp_tz_arg(self, tzstr):
    p = Period('1/1/2005', freq='M').to_timestamp(tz=tzstr)
    exp = Timestamp('1/1/2005', tz='UTC').tz_convert(tzstr)
    exp_zone = pytz.timezone(tzstr).normalize(p)
    assert p == exp
    assert p.tz == exp_zone.tzinfo
    assert p.tz == exp.tz
    p = Period('1/1/2005', freq='3H').to_timestamp(tz=tzstr)
    exp = Timestamp('1/1/2005', tz='UTC').tz_convert(tzstr)
    exp_zone = pytz.timezone(tzstr).normalize(p)
    assert p == exp
    assert p.tz == exp_zone.tzinfo
    assert p.tz == exp.tz
    p = Period('1/1/2005', freq='A').to_timestamp(freq='A', tz=tzstr)
    exp = Timestamp('31/12/2005', tz='UTC').tz_convert(tzstr)
    exp_zone = pytz.timezone(tzstr).normalize(p)
    assert p == exp
    assert p.tz == exp_zone.tzinfo
    assert p.tz == exp.tz
    p = Period('1/1/2005', freq='A').to_timestamp(freq='3H', tz=tzstr)
    exp = Timestamp('1/1/2005', tz='UTC').tz_convert(tzstr)
    exp_zone = pytz.timezone(tzstr).normalize(p)
    assert p == exp
    assert p.tz == exp_zone.tzinfo
    assert p.tz == exp.tz