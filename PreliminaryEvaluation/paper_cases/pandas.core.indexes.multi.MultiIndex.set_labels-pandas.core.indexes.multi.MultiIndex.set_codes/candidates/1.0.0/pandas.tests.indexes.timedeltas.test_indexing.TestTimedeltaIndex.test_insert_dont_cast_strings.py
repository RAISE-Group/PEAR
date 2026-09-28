def test_insert_dont_cast_strings(self):
    idx = timedelta_range('1day', '3day')
    result = idx.insert(0, '1 Day')
    assert result.dtype == object
    assert result[0] == '1 Day'