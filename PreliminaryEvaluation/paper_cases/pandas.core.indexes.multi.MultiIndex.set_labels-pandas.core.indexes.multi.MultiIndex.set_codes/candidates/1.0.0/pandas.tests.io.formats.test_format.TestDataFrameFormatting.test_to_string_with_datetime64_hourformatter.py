def test_to_string_with_datetime64_hourformatter(self):
    x = DataFrame({'hod': pd.to_datetime(['10:10:10.100', '12:12:12.120'], format='%H:%M:%S.%f')})

    def format_func(x):
        return x.strftime('%H:%M')
    result = x.to_string(formatters={'hod': format_func})
    expected = 'hod\n0 10:10\n1 12:12'
    assert result.strip() == expected