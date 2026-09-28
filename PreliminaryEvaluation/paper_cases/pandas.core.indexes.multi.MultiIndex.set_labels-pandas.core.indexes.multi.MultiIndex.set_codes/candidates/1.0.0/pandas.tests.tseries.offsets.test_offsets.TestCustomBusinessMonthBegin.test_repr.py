def test_repr(self):
    assert repr(self.offset) == '<CustomBusinessMonthBegin>'
    assert repr(self.offset2) == '<2 * CustomBusinessMonthBegins>'