@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_date_range_timezone_str_argument(self, tzstr):
    tz = timezones.maybe_get_tz(tzstr)
    result = date_range('1/1/2000', periods=10, tz=tzstr)
    expected = date_range('1/1/2000', periods=10, tz=tz)
    tm.assert_index_equal(result, expected)