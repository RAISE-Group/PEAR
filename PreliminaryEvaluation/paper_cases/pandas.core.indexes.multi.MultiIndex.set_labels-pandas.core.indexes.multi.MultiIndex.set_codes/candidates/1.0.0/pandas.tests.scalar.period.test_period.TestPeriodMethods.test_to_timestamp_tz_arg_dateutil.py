@pytest.mark.parametrize('tzstr', ['dateutil/Europe/Brussels', 'dateutil/Asia/Tokyo', 'dateutil/US/Pacific'])
def test_to_timestamp_tz_arg_dateutil(self, tzstr):
    tz = maybe_get_tz(tzstr)
    p = Period('1/1/2005', freq='M').to_timestamp(tz=tz)
    exp = Timestamp('1/1/2005', tz='UTC').tz_convert(tzstr)
    assert p == exp
    assert p.tz == dateutil_gettz(tzstr.split('/', 1)[1])
    assert p.tz == exp.tz
    p = Period('1/1/2005', freq='M').to_timestamp(freq='3H', tz=tz)
    exp = Timestamp('1/1/2005', tz='UTC').tz_convert(tzstr)
    assert p == exp
    assert p.tz == dateutil_gettz(tzstr.split('/', 1)[1])
    assert p.tz == exp.tz