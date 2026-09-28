@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_tz_convert_unsorted(self, tzstr):
    dr = date_range('2012-03-09', freq='H', periods=100, tz='utc')
    dr = dr.tz_convert(tzstr)
    result = dr[::-1].hour
    exp = dr.hour[::-1]
    tm.assert_almost_equal(result, exp)