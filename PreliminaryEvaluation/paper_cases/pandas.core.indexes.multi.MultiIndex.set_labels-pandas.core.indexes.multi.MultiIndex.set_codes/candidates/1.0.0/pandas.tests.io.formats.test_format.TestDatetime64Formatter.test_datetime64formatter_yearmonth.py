def test_datetime64formatter_yearmonth(self):
    x = Series([datetime(2016, 1, 1), datetime(2016, 2, 2)])

    def format_func(x):
        return x.strftime('%Y-%m')
    formatter = fmt.Datetime64Formatter(x, formatter=format_func)
    result = formatter.get_result()
    assert result == ['2016-01', '2016-02']