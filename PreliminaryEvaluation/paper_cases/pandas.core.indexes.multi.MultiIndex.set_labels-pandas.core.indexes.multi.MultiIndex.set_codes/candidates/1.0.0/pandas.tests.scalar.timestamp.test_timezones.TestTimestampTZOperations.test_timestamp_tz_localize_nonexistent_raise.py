@pytest.mark.parametrize('tz', ['Europe/Warsaw', 'dateutil/Europe/Warsaw'])
def test_timestamp_tz_localize_nonexistent_raise(self, tz):
    ts = Timestamp('2015-03-29 02:20:00')
    with pytest.raises(pytz.NonExistentTimeError):
        ts.tz_localize(tz, nonexistent='raise')
    with pytest.raises(ValueError):
        ts.tz_localize(tz, nonexistent='foo')