@pytest.mark.parametrize('tz', ['Europe/London', 'dateutil/Europe/London'])
def test_dti_construction_ambiguous_endpoint(self, tz):
    with pytest.raises(pytz.AmbiguousTimeError):
        date_range('2013-10-26 23:00', '2013-10-27 01:00', tz='Europe/London', freq='H')
    times = date_range('2013-10-26 23:00', '2013-10-27 01:00', freq='H', tz=tz, ambiguous='infer')
    assert times[0] == Timestamp('2013-10-26 23:00', tz=tz, freq='H')
    if str(tz).startswith('dateutil'):
        assert times[-1] == Timestamp('2013-10-27 01:00:00+0100', tz=tz, freq='H')
    else:
        assert times[-1] == Timestamp('2013-10-27 01:00:00+0000', tz=tz, freq='H')