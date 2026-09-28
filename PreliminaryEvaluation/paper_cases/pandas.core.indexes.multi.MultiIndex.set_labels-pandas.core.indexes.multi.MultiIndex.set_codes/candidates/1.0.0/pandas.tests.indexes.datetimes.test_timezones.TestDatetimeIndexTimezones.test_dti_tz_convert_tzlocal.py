def test_dti_tz_convert_tzlocal(self):
    dti = date_range(start='2001-01-01', end='2001-03-01', tz='UTC')
    dti2 = dti.tz_convert(dateutil.tz.tzlocal())
    tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)
    dti = date_range(start='2001-01-01', end='2001-03-01', tz=dateutil.tz.tzlocal())
    dti2 = dti.tz_convert(None)
    tm.assert_numpy_array_equal(dti2.asi8, dti.asi8)