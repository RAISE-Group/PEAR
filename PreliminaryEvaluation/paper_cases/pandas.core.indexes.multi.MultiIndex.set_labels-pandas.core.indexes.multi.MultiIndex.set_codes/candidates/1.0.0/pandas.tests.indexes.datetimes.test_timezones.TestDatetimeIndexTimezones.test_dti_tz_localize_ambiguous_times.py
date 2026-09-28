@pytest.mark.parametrize('tz', [pytz.timezone('US/Eastern'), gettz('US/Eastern')])
def test_dti_tz_localize_ambiguous_times(self, tz):
    dr = date_range(datetime(2011, 3, 13, 1, 30), periods=3, freq=pd.offsets.Hour())
    with pytest.raises(pytz.NonExistentTimeError):
        dr.tz_localize(tz)
    dr = date_range(datetime(2011, 3, 13, 3, 30), periods=3, freq=pd.offsets.Hour(), tz=tz)
    dr = date_range(datetime(2011, 11, 6, 1, 30), periods=3, freq=pd.offsets.Hour())
    with pytest.raises(pytz.AmbiguousTimeError):
        dr.tz_localize(tz)
    dr = date_range(datetime(2011, 3, 13), periods=48, freq=pd.offsets.Minute(30), tz=pytz.utc)