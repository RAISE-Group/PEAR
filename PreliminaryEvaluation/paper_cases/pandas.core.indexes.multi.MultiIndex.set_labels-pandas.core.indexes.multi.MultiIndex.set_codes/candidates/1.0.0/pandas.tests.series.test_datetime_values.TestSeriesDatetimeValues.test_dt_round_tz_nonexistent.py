@pytest.mark.parametrize('method, ts_str, freq', [['ceil', '2018-03-11 01:59:00-0600', '5min'], ['round', '2018-03-11 01:59:00-0600', '5min'], ['floor', '2018-03-11 03:01:00-0500', '2H']])
def test_dt_round_tz_nonexistent(self, method, ts_str, freq):
    s = Series([pd.Timestamp(ts_str, tz='America/Chicago')])
    result = getattr(s.dt, method)(freq, nonexistent='shift_forward')
    expected = Series([pd.Timestamp('2018-03-11 03:00:00', tz='America/Chicago')])
    tm.assert_series_equal(result, expected)
    result = getattr(s.dt, method)(freq, nonexistent='NaT')
    expected = Series([pd.NaT]).dt.tz_localize(result.dt.tz)
    tm.assert_series_equal(result, expected)
    with pytest.raises(pytz.NonExistentTimeError, match='2018-03-11 02:00:00'):
        getattr(s.dt, method)(freq, nonexistent='raise')