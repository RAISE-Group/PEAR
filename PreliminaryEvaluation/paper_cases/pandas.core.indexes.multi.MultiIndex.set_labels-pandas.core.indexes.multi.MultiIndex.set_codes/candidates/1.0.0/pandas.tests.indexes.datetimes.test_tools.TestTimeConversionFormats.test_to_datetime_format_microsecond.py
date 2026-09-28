@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_format_microsecond(self, cache):
    lang, _ = locale.getlocale()
    month_abbr = calendar.month_abbr[4]
    val = '01-{}-2011 00:00:01.978'.format(month_abbr)
    format = '%d-%b-%Y %H:%M:%S.%f'
    result = to_datetime(val, format=format, cache=cache)
    exp = datetime.strptime(val, format)
    assert result == exp