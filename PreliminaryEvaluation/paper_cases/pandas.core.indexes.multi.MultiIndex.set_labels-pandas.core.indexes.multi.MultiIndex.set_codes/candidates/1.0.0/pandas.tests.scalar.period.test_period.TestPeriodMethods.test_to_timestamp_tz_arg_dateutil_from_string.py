def test_to_timestamp_tz_arg_dateutil_from_string(self):
    p = Period('1/1/2005', freq='M').to_timestamp(tz='dateutil/Europe/Brussels')
    assert p.tz == dateutil_gettz('Europe/Brussels')