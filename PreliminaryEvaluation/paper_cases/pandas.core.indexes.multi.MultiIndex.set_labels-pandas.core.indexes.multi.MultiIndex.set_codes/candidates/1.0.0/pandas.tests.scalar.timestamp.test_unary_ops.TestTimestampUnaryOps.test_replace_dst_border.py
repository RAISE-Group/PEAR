def test_replace_dst_border(self):
    t = Timestamp('2013-11-3', tz='America/Chicago')
    result = t.replace(hour=3)
    expected = Timestamp('2013-11-3 03:00:00', tz='America/Chicago')
    assert result == expected