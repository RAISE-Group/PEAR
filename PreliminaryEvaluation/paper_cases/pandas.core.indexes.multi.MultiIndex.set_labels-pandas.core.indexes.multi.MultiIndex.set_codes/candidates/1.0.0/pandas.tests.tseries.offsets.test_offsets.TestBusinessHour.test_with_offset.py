def test_with_offset(self):
    expected = Timestamp('2014-07-01 13:00')
    assert self.d + BusinessHour() * 3 == expected
    assert self.d + BusinessHour(n=3) == expected