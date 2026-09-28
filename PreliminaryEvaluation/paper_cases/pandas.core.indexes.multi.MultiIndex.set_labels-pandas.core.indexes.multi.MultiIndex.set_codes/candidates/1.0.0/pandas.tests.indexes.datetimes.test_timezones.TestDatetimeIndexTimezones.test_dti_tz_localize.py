@pytest.mark.parametrize('prefix', ['', 'dateutil/'])
def test_dti_tz_localize(self, prefix):
    tzstr = prefix + 'US/Eastern'
    dti = pd.date_range(start='1/1/2005', end='1/1/2005 0:00:30.256', freq='L')
    dti2 = dti.tz_localize(tzstr)
    dti_utc = pd.date_range(start='1/1/2005 05:00', end='1/1/2005 5:00:30.256', freq='L', tz='utc')
    tm.assert_numpy_array_equal(dti2.values, dti_utc.values)
    dti3 = dti2.tz_convert(prefix + 'US/Pacific')
    tm.assert_numpy_array_equal(dti3.values, dti_utc.values)
    dti = pd.date_range(start='11/6/2011 1:59', end='11/6/2011 2:00', freq='L')
    with pytest.raises(pytz.AmbiguousTimeError):
        dti.tz_localize(tzstr)
    dti = pd.date_range(start='3/13/2011 1:59', end='3/13/2011 2:00', freq='L')
    with pytest.raises(pytz.NonExistentTimeError):
        dti.tz_localize(tzstr)