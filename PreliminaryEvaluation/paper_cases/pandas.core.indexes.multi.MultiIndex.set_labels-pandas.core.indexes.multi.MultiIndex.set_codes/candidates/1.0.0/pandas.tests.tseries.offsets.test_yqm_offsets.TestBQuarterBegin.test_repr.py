def test_repr(self):
    expected = '<BusinessQuarterBegin: startingMonth=3>'
    assert repr(BQuarterBegin()) == expected
    expected = '<BusinessQuarterBegin: startingMonth=3>'
    assert repr(BQuarterBegin(startingMonth=3)) == expected
    expected = '<BusinessQuarterBegin: startingMonth=1>'
    assert repr(BQuarterBegin(startingMonth=1)) == expected