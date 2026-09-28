@pytest.mark.parametrize('tz', ['US/Eastern', 'dateutil/US/Eastern', pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_tz_localize_utc_conversion(self, tz):
    rng = date_range('3/10/2012', '3/11/2012', freq='30T')
    converted = rng.tz_localize(tz)
    expected_naive = rng + pd.offsets.Hour(5)
    tm.assert_numpy_array_equal(converted.asi8, expected_naive.asi8)
    rng = date_range('3/11/2012', '3/12/2012', freq='30T')
    with pytest.raises(pytz.NonExistentTimeError):
        rng.tz_localize(tz)