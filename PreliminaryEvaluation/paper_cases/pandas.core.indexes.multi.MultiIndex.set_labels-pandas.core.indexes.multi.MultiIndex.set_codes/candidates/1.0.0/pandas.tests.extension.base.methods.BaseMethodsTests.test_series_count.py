def test_series_count(self, data_missing):
    ser = pd.Series(data_missing)
    result = ser.count()
    expected = 1
    assert result == expected