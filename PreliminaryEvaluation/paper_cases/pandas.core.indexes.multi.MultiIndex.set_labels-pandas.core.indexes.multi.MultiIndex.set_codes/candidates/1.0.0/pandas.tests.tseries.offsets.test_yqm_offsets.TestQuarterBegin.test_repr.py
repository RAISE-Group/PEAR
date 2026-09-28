def test_repr(self):
    expected = '<QuarterBegin: startingMonth=3>'
    assert repr(QuarterBegin()) == expected
    expected = '<QuarterBegin: startingMonth=3>'
    assert repr(QuarterBegin(startingMonth=3)) == expected
    expected = '<QuarterBegin: startingMonth=1>'
    assert repr(QuarterBegin(startingMonth=1)) == expected