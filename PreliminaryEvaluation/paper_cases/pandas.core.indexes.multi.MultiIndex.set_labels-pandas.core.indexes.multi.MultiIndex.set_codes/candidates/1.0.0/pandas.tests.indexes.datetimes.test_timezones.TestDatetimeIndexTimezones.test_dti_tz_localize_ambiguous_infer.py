@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_tz_localize_ambiguous_infer(self, tz):
    dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour())
    with pytest.raises(pytz.AmbiguousTimeError):
        dr.tz_localize(tz)
    dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour(), tz=tz)
    times = ['11/06/2011 00:00', '11/06/2011 01:00', '11/06/2011 01:00', '11/06/2011 02:00', '11/06/2011 03:00']
    di = DatetimeIndex(times)
    localized = di.tz_localize(tz, ambiguous='infer')
    tm.assert_index_equal(dr, localized)
    tm.assert_index_equal(dr, DatetimeIndex(times, tz=tz, ambiguous='infer'))
    dr = date_range(datetime(2011, 6, 1, 0), periods=10, freq=pd.offsets.Hour())
    localized = dr.tz_localize(tz)
    localized_infer = dr.tz_localize(tz, ambiguous='infer')
    tm.assert_index_equal(localized, localized_infer)