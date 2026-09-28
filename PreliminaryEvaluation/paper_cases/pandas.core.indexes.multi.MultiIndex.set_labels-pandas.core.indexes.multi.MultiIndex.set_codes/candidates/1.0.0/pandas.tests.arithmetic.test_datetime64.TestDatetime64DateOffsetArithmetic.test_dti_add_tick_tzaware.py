def test_dti_add_tick_tzaware(self, tz_aware_fixture, box_with_array):
    tz = tz_aware_fixture
    if tz == 'US/Pacific':
        dates = date_range('2012-11-01', periods=3, tz=tz)
        offset = dates + pd.offsets.Hour(5)
        assert dates[0] + pd.offsets.Hour(5) == offset[0]
    dates = date_range('2010-11-01 00:00', periods=3, tz=tz, freq='H')
    expected = DatetimeIndex(['2010-11-01 05:00', '2010-11-01 06:00', '2010-11-01 07:00'], freq='H', tz=tz)
    dates = tm.box_expected(dates, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    offset = dates + pd.offsets.Hour(5)
    tm.assert_equal(offset, expected)
    offset = dates + np.timedelta64(5, 'h')
    tm.assert_equal(offset, expected)
    offset = dates + timedelta(hours=5)
    tm.assert_equal(offset, expected)