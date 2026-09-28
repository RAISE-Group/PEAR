def test_to_string_with_datetime64_monthformatter(self):
    months = [datetime(2016, 1, 1), datetime(2016, 2, 2)]
    x = DataFrame({'months': months})

    def format_func(x):
        return x.strftime('%Y-%m')
    result = x.to_string(formatters={'months': format_func})
    expected = 'months\n0 2016-01\n1 2016-02'
    assert result.strip() == expected