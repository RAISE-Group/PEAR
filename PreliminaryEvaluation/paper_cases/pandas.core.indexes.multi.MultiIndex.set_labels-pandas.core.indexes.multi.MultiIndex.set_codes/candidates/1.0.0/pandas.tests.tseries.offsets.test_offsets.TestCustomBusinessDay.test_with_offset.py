def test_with_offset(self):
    offset = self.offset + timedelta(hours=2)
    assert self.d + offset == datetime(2008, 1, 2, 2)