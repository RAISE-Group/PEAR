def test_processing_order(self):
    result = pd.to_datetime(200 * 365, unit='D')
    expected = Timestamp('2169-11-13 00:00:00')
    assert result == expected
    result = pd.to_datetime(200 * 365, unit='D', origin='1870-01-01')
    expected = Timestamp('2069-11-13 00:00:00')
    assert result == expected
    result = pd.to_datetime(300 * 365, unit='D', origin='1870-01-01')
    expected = Timestamp('2169-10-20 00:00:00')
    assert result == expected