def test_repr(self):
    expected = '<BusinessQuarterEnd: startingMonth=3>'
    assert repr(BQuarterEnd()) == expected
    expected = '<BusinessQuarterEnd: startingMonth=3>'
    assert repr(BQuarterEnd(startingMonth=3)) == expected
    expected = '<BusinessQuarterEnd: startingMonth=1>'
    assert repr(BQuarterEnd(startingMonth=1)) == expected