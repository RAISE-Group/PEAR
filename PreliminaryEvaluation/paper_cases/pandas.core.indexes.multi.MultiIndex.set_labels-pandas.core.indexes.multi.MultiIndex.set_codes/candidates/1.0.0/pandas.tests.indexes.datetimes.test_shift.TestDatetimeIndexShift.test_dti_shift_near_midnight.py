@pytest.mark.parametrize('shift, result_time', [[0, '2014-11-14 00:00:00'], [-1, '2014-11-13 23:00:00'], [1, '2014-11-14 01:00:00']])
def test_dti_shift_near_midnight(self, shift, result_time):
    dt = datetime(2014, 11, 14, 0)
    dt_est = pytz.timezone('EST').localize(dt)
    s = Series(data=[1], index=[dt_est])
    result = s.shift(shift, freq='H')
    expected = Series(1, index=DatetimeIndex([result_time], tz='EST'))
    tm.assert_series_equal(result, expected)