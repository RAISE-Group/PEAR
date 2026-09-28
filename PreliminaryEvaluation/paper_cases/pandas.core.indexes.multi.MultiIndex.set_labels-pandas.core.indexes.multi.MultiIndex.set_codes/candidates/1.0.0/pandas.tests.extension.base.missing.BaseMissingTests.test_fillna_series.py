def test_fillna_series(self, data_missing):
    fill_value = data_missing[1]
    ser = pd.Series(data_missing)
    result = ser.fillna(fill_value)
    expected = pd.Series(data_missing._from_sequence([fill_value, fill_value], dtype=data_missing.dtype))
    self.assert_series_equal(result, expected)
    result = ser.fillna(expected)
    self.assert_series_equal(result, expected)
    result = ser.fillna(ser)
    self.assert_series_equal(result, ser)