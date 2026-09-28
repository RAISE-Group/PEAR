@pytest.mark.parametrize('klass', [DatetimeIndex, DatetimeArray])
def test_to_datetime_dta_tz(self, klass):
    dti = date_range('2015-04-05', periods=3).rename('foo')
    expected = dti.tz_localize('UTC')
    obj = klass(dti)
    expected = klass(expected)
    result = to_datetime(obj, utc=True)
    tm.assert_equal(result, expected)