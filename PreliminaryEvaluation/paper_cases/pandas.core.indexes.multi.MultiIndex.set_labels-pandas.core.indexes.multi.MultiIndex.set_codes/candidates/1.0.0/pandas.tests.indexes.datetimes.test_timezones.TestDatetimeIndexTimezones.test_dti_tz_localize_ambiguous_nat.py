@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_tz_localize_ambiguous_nat(self, tz):
    times = ['11/06/2011 00:00', '11/06/2011 01:00', '11/06/2011 01:00', '11/06/2011 02:00', '11/06/2011 03:00']
    di = DatetimeIndex(times)
    localized = di.tz_localize(tz, ambiguous='NaT')
    times = ['11/06/2011 00:00', np.NaN, np.NaN, '11/06/2011 02:00', '11/06/2011 03:00']
    di_test = DatetimeIndex(times, tz='US/Eastern')
    tm.assert_numpy_array_equal(di_test.values, localized.values)