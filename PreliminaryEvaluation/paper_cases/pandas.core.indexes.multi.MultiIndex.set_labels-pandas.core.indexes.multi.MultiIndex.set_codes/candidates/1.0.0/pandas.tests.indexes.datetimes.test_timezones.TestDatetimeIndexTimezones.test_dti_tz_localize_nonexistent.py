@pytest.mark.parametrize('tz', ['Europe/Warsaw', 'dateutil/Europe/Warsaw'])
@pytest.mark.parametrize('method, exp', [['NaT', pd.NaT], ['raise', None], ['foo', 'invalid']])
def test_dti_tz_localize_nonexistent(self, tz, method, exp):
    n = 60
    dti = date_range(start='2015-03-29 02:00:00', periods=n, freq='min')
    if method == 'raise':
        with pytest.raises(pytz.NonExistentTimeError):
            dti.tz_localize(tz, nonexistent=method)
    elif exp == 'invalid':
        with pytest.raises(ValueError):
            dti.tz_localize(tz, nonexistent=method)
    else:
        result = dti.tz_localize(tz, nonexistent=method)
        expected = DatetimeIndex([exp] * n, tz=tz)
        tm.assert_index_equal(result, expected)