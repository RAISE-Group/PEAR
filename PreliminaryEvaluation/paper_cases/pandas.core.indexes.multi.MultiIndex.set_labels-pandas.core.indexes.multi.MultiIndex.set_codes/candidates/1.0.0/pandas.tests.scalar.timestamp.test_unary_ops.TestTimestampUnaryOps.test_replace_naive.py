def test_replace_naive(self):
    ts = Timestamp('2016-01-01 09:00:00')
    result = ts.replace(hour=0)
    expected = Timestamp('2016-01-01 00:00:00')
    assert result == expected