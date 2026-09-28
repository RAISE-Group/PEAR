def test_repr(self):
    assert repr(self.offset) == '<CustomBusinessMonthEnd>'
    assert repr(self.offset2) == '<2 * CustomBusinessMonthEnds>'