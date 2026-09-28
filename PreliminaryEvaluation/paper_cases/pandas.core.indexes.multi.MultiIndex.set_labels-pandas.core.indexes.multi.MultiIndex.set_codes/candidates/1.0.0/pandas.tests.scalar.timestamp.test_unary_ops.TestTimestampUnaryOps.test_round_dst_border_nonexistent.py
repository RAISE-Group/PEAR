@pytest.mark.parametrize('method, ts_str, freq', [['ceil', '2018-03-11 01:59:00-0600', '5min'], ['round', '2018-03-11 01:59:00-0600', '5min'], ['floor', '2018-03-11 03:01:00-0500', '2H']])
def test_round_dst_border_nonexistent(self, method, ts_str, freq):
    ts = Timestamp(ts_str, tz='America/Chicago')
    result = getattr(ts, method)(freq, nonexistent='shift_forward')
    expected = Timestamp('2018-03-11 03:00:00', tz='America/Chicago')
    assert result == expected
    result = getattr(ts, method)(freq, nonexistent='NaT')
    assert result is NaT
    with pytest.raises(pytz.NonExistentTimeError, match='2018-03-11 02:00:00'):
        getattr(ts, method)(freq, nonexistent='raise')