def test_normalize(self):
    dt = datetime(2007, 1, 1, 3)
    result = dt + MonthEnd(normalize=True)
    expected = dt.replace(hour=0) + MonthEnd()
    assert result == expected