def test_normalize(self):
    dt = datetime(2007, 1, 1, 3)
    result = dt + BMonthEnd(normalize=True)
    expected = dt.replace(hour=0) + BMonthEnd()
    assert result == expected