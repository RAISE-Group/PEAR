@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_astimezone(self, tzstr):
    utcdate = Timestamp('3/11/2012 22:00', tz='UTC')
    expected = utcdate.tz_convert(tzstr)
    result = utcdate.astimezone(tzstr)
    assert expected == result
    assert isinstance(result, Timestamp)