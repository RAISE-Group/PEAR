@pytest.mark.parametrize('tz, option, expected', [['US/Pacific', 'shift_forward', '2019-03-10 03:00'], ['dateutil/US/Pacific', 'shift_forward', '2019-03-10 03:00'], ['US/Pacific', 'shift_backward', '2019-03-10 01:00'], pytest.param('dateutil/US/Pacific', 'shift_backward', '2019-03-10 01:00', marks=pytest.mark.xfail(reason='GH 24329')), ['US/Pacific', timedelta(hours=1), '2019-03-10 03:00']])
def test_dti_construction_nonexistent_endpoint(self, tz, option, expected):
    with pytest.raises(pytz.NonExistentTimeError):
        date_range('2019-03-10 00:00', '2019-03-10 02:00', tz='US/Pacific', freq='H')
    times = date_range('2019-03-10 00:00', '2019-03-10 02:00', freq='H', tz=tz, nonexistent=option)
    assert times[-1] == Timestamp(expected, tz=tz, freq='H')