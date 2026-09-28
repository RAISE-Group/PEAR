def test_tz_localize_ambiguous_compat(self):
    naive = Timestamp('2013-10-27 01:00:00')
    pytz_zone = 'Europe/London'
    dateutil_zone = 'dateutil/Europe/London'
    result_pytz = naive.tz_localize(pytz_zone, ambiguous=0)
    result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=0)
    assert result_pytz.value == result_dateutil.value
    assert result_pytz.value == 1382835600000000000
    assert result_pytz.to_pydatetime().tzname() == 'GMT'
    assert result_dateutil.to_pydatetime().tzname() == 'BST'
    assert str(result_pytz) != str(result_dateutil)
    result_pytz = naive.tz_localize(pytz_zone, ambiguous=1)
    result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=1)
    assert result_pytz.value == result_dateutil.value
    assert result_pytz.value == 1382832000000000000
    assert str(result_pytz) == str(result_dateutil)
    assert result_pytz.to_pydatetime().tzname() == result_dateutil.to_pydatetime().tzname()