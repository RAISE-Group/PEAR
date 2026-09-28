def test_format_datetime_with_time(self):
    t = Index([datetime(2012, 2, 7), datetime(2012, 2, 7, 23)])
    result = t.format()
    expected = ['2012-02-07 00:00:00', '2012-02-07 23:00:00']
    assert len(result) == 2
    assert result == expected