def test_millisecond_repr(self):
    p = Period('2000-01-01 12:15:02.123')
    assert repr(p) == "Period('2000-01-01 12:15:02.123', 'L')"