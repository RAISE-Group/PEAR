def test_microsecond_repr(self):
    p = Period('2000-01-01 12:15:02.123567')
    assert repr(p) == "Period('2000-01-01 12:15:02.123567', 'U')"