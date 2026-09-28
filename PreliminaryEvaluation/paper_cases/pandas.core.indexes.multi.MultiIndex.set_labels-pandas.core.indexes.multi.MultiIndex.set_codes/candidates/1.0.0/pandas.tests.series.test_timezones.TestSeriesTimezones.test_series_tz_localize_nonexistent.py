@pytest.mark.parametrize('tz', ['Europe/Warsaw', 'dateutil/Europe/Warsaw'])
@pytest.mark.parametrize('method, exp', [['shift_forward', '2015-03-29 03:00:00'], ['NaT', NaT], ['raise', None], ['foo', 'invalid']])
def test_series_tz_localize_nonexistent(self, tz, method, exp):
    n = 60
    dti = date_range(start='2015-03-29 02:00:00', periods=n, freq='min')
    s = Series(1, dti)
    if method == 'raise':
        with pytest.raises(pytz.NonExistentTimeError):
            s.tz_localize(tz, nonexistent=method)
    elif exp == 'invalid':
        with pytest.raises(ValueError):
            dti.tz_localize(tz, nonexistent=method)
    else:
        result = s.tz_localize(tz, nonexistent=method)
        expected = Series(1, index=DatetimeIndex([exp] * n, tz=tz))
        tm.assert_series_equal(result, expected)