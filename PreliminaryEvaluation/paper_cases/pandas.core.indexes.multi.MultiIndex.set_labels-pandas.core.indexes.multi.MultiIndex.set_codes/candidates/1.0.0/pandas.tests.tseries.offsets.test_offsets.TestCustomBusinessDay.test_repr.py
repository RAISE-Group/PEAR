def test_repr(self):
    assert repr(self.offset) == '<CustomBusinessDay>'
    assert repr(self.offset2) == '<2 * CustomBusinessDays>'
    if compat.PY37:
        expected = '<BusinessDay: offset=datetime.timedelta(days=1)>'
    else:
        expected = '<BusinessDay: offset=datetime.timedelta(1)>'
    assert repr(self.offset + timedelta(1)) == expected