def test_format_with_name_time_info(self):
    dates = date_range('2011-01-01 04:00:00', periods=10, name='something')
    formatted = dates.format(name=True)
    assert formatted[0] == 'something'