@pytest.mark.parametrize('data', [Timestamp('2017-08-28 23:00:00'), Timestamp('2017-08-28 23:00:00', tz='EST')])
@pytest.mark.parametrize('time_locale', [None] if tm.get_locales() is None else [None] + tm.get_locales())
def test_names(self, data, time_locale):
    if time_locale is None:
        expected_day = 'Monday'
        expected_month = 'August'
    else:
        with tm.set_locale(time_locale, locale.LC_TIME):
            expected_day = calendar.day_name[0].capitalize()
            expected_month = calendar.month_name[8].capitalize()
    result_day = data.day_name(time_locale)
    result_month = data.month_name(time_locale)
    expected_day = unicodedata.normalize('NFD', expected_day)
    expected_month = unicodedata.normalize('NFD', expected_month)
    result_day = unicodedata.normalize('NFD', result_day)
    result_month = unicodedata.normalize('NFD', result_month)
    assert result_day == expected_day
    assert result_month == expected_month
    nan_ts = Timestamp(NaT)
    assert np.isnan(nan_ts.day_name(time_locale))
    assert np.isnan(nan_ts.month_name(time_locale))