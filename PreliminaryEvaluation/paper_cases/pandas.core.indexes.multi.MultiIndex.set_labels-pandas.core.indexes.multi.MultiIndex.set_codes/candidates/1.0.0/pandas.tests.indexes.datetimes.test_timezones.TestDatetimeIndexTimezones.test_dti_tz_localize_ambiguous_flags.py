@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_tz_localize_ambiguous_flags(self, tz):
    dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=pd.offsets.Hour(), tz=tz)
    times = ['11/06/2011 00:00', '11/06/2011 01:00', '11/06/2011 01:00', '11/06/2011 02:00', '11/06/2011 03:00']
    di = DatetimeIndex(times)
    is_dst = [1, 1, 0, 0, 0]
    localized = di.tz_localize(tz, ambiguous=is_dst)
    tm.assert_index_equal(dr, localized)
    tm.assert_index_equal(dr, DatetimeIndex(times, tz=tz, ambiguous=is_dst))
    localized = di.tz_localize(tz, ambiguous=np.array(is_dst))
    tm.assert_index_equal(dr, localized)
    localized = di.tz_localize(tz, ambiguous=np.array(is_dst).astype('bool'))
    tm.assert_index_equal(dr, localized)
    localized = DatetimeIndex(times, tz=tz, ambiguous=is_dst)
    tm.assert_index_equal(dr, localized)
    times += times
    di = DatetimeIndex(times)
    with pytest.raises(Exception):
        di.tz_localize(tz, ambiguous=is_dst)
    is_dst = np.hstack((is_dst, is_dst))
    localized = di.tz_localize(tz, ambiguous=is_dst)
    dr = dr.append(dr)
    tm.assert_index_equal(dr, localized)
    dr = date_range(datetime(2011, 6, 1, 0), periods=10, freq=pd.offsets.Hour())
    is_dst = np.array([1] * 10)
    localized = dr.tz_localize(tz)
    localized_is_dst = dr.tz_localize(tz, ambiguous=is_dst)
    tm.assert_index_equal(localized, localized_is_dst)